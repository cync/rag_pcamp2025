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
        vector_store = VectorStore()
        
        # Buscar todas as palestras únicas
        # Usar uma busca genérica para obter metadados
        try:
            # Tentar buscar alguns pontos para obter metadados
            search_results = vector_store.client.scroll(
                collection_name=vector_store.collection_name,
                limit=1000,  # Buscar muitos para ter todas as palestras
                with_payload=True,
                with_vectors=False
            )
            
            # Extrair palestras únicas
            palestras_map = {}
            for point in search_results[0]:  # search_results é uma tupla (points, next_page_offset)
                payload = point.payload
                titulo = payload.get("titulo_palestra", "Desconhecido")
                
                if titulo not in palestras_map:
                    palestras_map[titulo] = {
                        "titulo_palestra": titulo,
                        "palestrante": payload.get("palestrante", "Desconhecido"),
                        "tipo": payload.get("tipo", "palestra"),
                        "tema": payload.get("tema"),
                        "dia": payload.get("dia"),
                    }
            
            palestras = list(palestras_map.values())
            logger.info(f"Encontradas {len(palestras)} palestras únicas")
            
            return palestras
            
        except Exception as e:
            logger.warning(f"Erro ao buscar palestras: {str(e)}")
            # Retornar lista vazia se não conseguir buscar
            return []
    
    except Exception as e:
        logger.error(f"Erro ao listar palestras: {str(e)}", exc_info=True)
        return []

