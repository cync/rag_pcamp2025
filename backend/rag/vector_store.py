"""
Vector Store - Interface com Qdrant
"""
import os
import logging
from typing import List, Dict, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Filter, FieldCondition, MatchValue, Distance, VectorParams
)

logger = logging.getLogger(__name__)


class VectorStore:
    """
    Cliente para interagir com Qdrant.
    
    Responsável por:
    - Buscar chunks relevantes
    - Aplicar filtros por metadados
    - Gerenciar conexão com Qdrant
    """
    
    def __init__(self):
        """Inicializar cliente Qdrant"""
        self.host = os.getenv("QDRANT_HOST", "localhost")
        self.port = int(os.getenv("QDRANT_PORT", "6333"))
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "product_camp_2025")
        
        try:
            self.client = QdrantClient(host=self.host, port=self.port)
            logger.info(f"Conectado ao Qdrant em {self.host}:{self.port}")
            
            # Verificar se a collection existe
            collections = self.client.get_collections().collections
            collection_names = [c.name for c in collections]
            
            if self.collection_name not in collection_names:
                logger.warning(
                    f"Collection '{self.collection_name}' não encontrada. "
                    "Execute o script de ingestão primeiro."
                )
        
        except Exception as e:
            logger.error(f"Erro ao conectar ao Qdrant: {str(e)}")
            raise
    
    def search(
        self,
        query_vector: List[float],
        top_k: int = 5,
        filters: Optional[Dict[str, str]] = None
    ) -> List[Dict]:
        """
        Buscar chunks relevantes.
        
        Args:
            query_vector: Vetor de embedding da query
            top_k: Número de resultados a retornar
            filters: Filtros opcionais por metadados
        
        Returns:
            Lista de chunks com texto e metadados
        """
        try:
            # Construir filtros
            query_filter = None
            if filters:
                conditions = []
                
                if "palestrante" in filters:
                    conditions.append(
                        FieldCondition(
                            key="palestrante",
                            match=MatchValue(value=filters["palestrante"])
                        )
                    )
                
                if "tema" in filters:
                    conditions.append(
                        FieldCondition(
                            key="tema",
                            match=MatchValue(value=filters["tema"])
                        )
                    )
                
                if "tipo" in filters:
                    conditions.append(
                        FieldCondition(
                            key="tipo",
                            match=MatchValue(value=filters["tipo"])
                        )
                    )
                
                if conditions:
                    query_filter = Filter(must=conditions)
            
            # Buscar no Qdrant
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=top_k,
                query_filter=query_filter,
                score_threshold=0.3  # Threshold mínimo de relevância
            )
            
            # Formatar resultados
            results = []
            for result in search_results:
                # Reconstruir estrutura de metadados
                metadata = {
                    "titulo_palestra": result.payload.get("titulo_palestra", "N/A"),
                    "palestrante": result.payload.get("palestrante", "N/A"),
                    "tipo": result.payload.get("tipo", "N/A"),
                    "tema": result.payload.get("tema"),
                    "pagina_ou_slide": result.payload.get("pagina_ou_slide"),
                    "fonte": result.payload.get("fonte", "Product Camp 2025")
                }
                results.append({
                    "text": result.payload.get("text", ""),
                    "metadata": metadata,
                    "score": result.score
                })
            
            logger.debug(f"Encontrados {len(results)} chunks relevantes")
            return results
        
        except Exception as e:
            logger.error(f"Erro ao buscar no Qdrant: {str(e)}", exc_info=True)
            return []
    
    def create_collection_if_not_exists(self, vector_size: int = 1536):
        """
        Criar collection no Qdrant se não existir.
        
        Args:
            vector_size: Dimensão dos vetores (1536 para OpenAI text-embedding-ada-002)
        """
        try:
            collections = self.client.get_collections().collections
            collection_names = [c.name for c in collections]
            
            if self.collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                        size=vector_size,
                        distance=Distance.COSINE
                    )
                )
                logger.info(f"Collection '{self.collection_name}' criada com sucesso")
            else:
                logger.info(f"Collection '{self.collection_name}' já existe")
        
        except Exception as e:
            logger.error(f"Erro ao criar collection: {str(e)}")
            raise

