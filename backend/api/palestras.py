"""
Endpoint para listar palestras disponíveis
"""
from fastapi import APIRouter
from typing import List, Dict
import logging
from rag.vector_store import VectorStore

logger = logging.getLogger(__name__)

palestras_router = APIRouter()


@palestras_router.get("/palestras", response_model=List[Dict[str, str]])
async def list_palestras():
    """
    Lista todas as palestras disponíveis no sistema.
    Retorna lista única de palestras com metadados.
    """
    try:
        logger.info("Iniciando busca de palestras...")
        vector_store = VectorStore()
        
        # Verificar se a collection existe
        try:
            collections = vector_store.client.get_collections().collections
            collection_names = [c.name for c in collections]
            if vector_store.collection_name not in collection_names:
                logger.warning(f"Collection '{vector_store.collection_name}' não encontrada")
                return []
        except Exception as e:
            logger.error(f"Erro ao verificar collections: {str(e)}")
            return []
        
        # Buscar todas as palestras únicas
        try:
            logger.info(f"Buscando pontos na collection '{vector_store.collection_name}'...")
            search_results = vector_store.client.scroll(
                collection_name=vector_store.collection_name,
                limit=1000,  # Buscar muitos para ter todas as palestras
                with_payload=True,
                with_vectors=False
            )
            
            points = search_results[0]  # search_results é uma tupla (points, next_page_offset)
            logger.info(f"Encontrados {len(points)} pontos no Qdrant")
            
            if not points:
                logger.warning("Nenhum ponto encontrado no Qdrant")
                return []
            
            # Extrair palestras únicas
            palestras_map = {}
            for point in points:
                payload = point.payload
                titulo = payload.get("titulo_palestra", "Desconhecido")
                
                if titulo and titulo != "Desconhecido" and titulo not in palestras_map:
                    palestras_map[titulo] = {
                        "titulo_palestra": titulo,
                        "palestrante": payload.get("palestrante", "Desconhecido"),
                        "tipo": payload.get("tipo", "palestra"),
                        "tema": payload.get("tema"),
                        "dia": payload.get("dia"),
                    }
            
            palestras = list(palestras_map.values())
            logger.info(f"Encontradas {len(palestras)} palestras únicas: {[p['titulo_palestra'] for p in palestras]}")
            
            return palestras
            
        except Exception as e:
            logger.error(f"Erro ao buscar palestras do Qdrant: {str(e)}", exc_info=True)
            return []
    
    except Exception as e:
        logger.error(f"Erro ao listar palestras: {str(e)}", exc_info=True)
        return []

