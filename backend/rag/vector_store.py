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
        # Suportar Qdrant Cloud (URL + API Key) ou Qdrant local (host:port)
        qdrant_url = os.getenv("QDRANT_URL")
        qdrant_api_key = os.getenv("QDRANT_API_KEY")
        self.host = os.getenv("QDRANT_HOST", "localhost")
        self.port = int(os.getenv("QDRANT_PORT", "6333"))
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "product_camp_2025")
        
        try:
            # Prioridade 1: Qdrant Cloud (URL + API Key)
            if qdrant_url and qdrant_api_key:
                # Qdrant Cloud usa URL completa com https://
                if not qdrant_url.startswith("http"):
                    qdrant_url = f"https://{qdrant_url}"
                
                self.client = QdrantClient(
                    url=qdrant_url,
                    api_key=qdrant_api_key,
                    timeout=10,
                    prefer_grpc=False
                )
                logger.info(f"Conectando ao Qdrant Cloud: {qdrant_url}")
                logger.info("Usando autenticação com API Key")
            
            # Prioridade 2: URL sem API Key (pode ser Railway ou local)
            elif qdrant_url:
                # Se a URL começa com http/https, usar como URL completa
                if qdrant_url.startswith("http://") or qdrant_url.startswith("https://"):
                    self.client = QdrantClient(
                        url=qdrant_url,
                        prefer_grpc=False,
                        timeout=10
                    )
                    logger.info(f"Conectando ao Qdrant via URL: {qdrant_url}")
                else:
                    # Remover http:// ou https:// se presente para host:port
                    qdrant_url_clean = qdrant_url.replace("http://", "").replace("https://", "")
                    if ":" in qdrant_url_clean:
                        self.host, port_str = qdrant_url_clean.split(":", 1)
                        self.port = int(port_str)
                    else:
                        self.host = qdrant_url_clean
                    
                    self.client = QdrantClient(
                        host=self.host, 
                        port=self.port,
                        prefer_grpc=False,
                        timeout=10
                    )
                    logger.info(f"Conectando ao Qdrant em {self.host}:{self.port}")
            
            # Prioridade 3: Host:Port (local ou Railway service)
            else:
                self.client = QdrantClient(
                    host=self.host, 
                    port=self.port,
                    prefer_grpc=False,
                    timeout=10
                )
                logger.info(f"Conectando ao Qdrant em {self.host}:{self.port}")
                logger.warning("Usando host:port. Se você tem Qdrant Cloud, configure QDRANT_URL e QDRANT_API_KEY")
            
            # Verificar se a collection existe (pode não existir ainda)
            # Não falhar se não conseguir conectar - pode ser que o Qdrant ainda não esteja pronto
            try:
                collections = self.client.get_collections().collections
                collection_names = [c.name for c in collections]
                
                if self.collection_name not in collection_names:
                    logger.warning(
                        f"Collection '{self.collection_name}' não encontrada. "
                        "Execute o script de ingestão primeiro."
                    )
                else:
                    logger.info(f"Collection '{self.collection_name}' encontrada")
            except Exception as e:
                error_msg = str(e)
                logger.warning(f"Não foi possível verificar collections: {error_msg}")
                
                # Diagnóstico mais detalhado
                if "404" in error_msg or "Not Found" in error_msg:
                    logger.warning("Erro 404: Verifique se:")
                    logger.warning("  1. QDRANT_URL está correto (URL completa do cluster)")
                    logger.warning("  2. QDRANT_API_KEY está configurada (se usar Qdrant Cloud)")
                    logger.warning("  3. QDRANT_HOST está correto (se usar serviço Railway)")
                    if qdrant_url and qdrant_api_key:
                        logger.info(f"Configurado: QDRANT_URL={qdrant_url[:50]}..., QDRANT_API_KEY={'*' * 10}")
                    elif qdrant_url:
                        logger.info(f"Configurado: QDRANT_URL={qdrant_url}")
                    else:
                        logger.info(f"Configurado: QDRANT_HOST={self.host}, QDRANT_PORT={self.port}")
                
                logger.warning("A collection será criada automaticamente durante a ingestão.")
                # Não falhar aqui - permitir que a aplicação inicie mesmo sem Qdrant
        
        except Exception as e:
            logger.error(f"Erro ao conectar ao Qdrant em {self.host}:{self.port}: {str(e)}")
            logger.error("Verifique se:")
            logger.error("1. O serviço Qdrant está rodando no Railway")
            logger.error("2. QDRANT_HOST está configurado corretamente (nome do serviço)")
            logger.error("3. QDRANT_PORT está configurado (geralmente 6333)")
            logger.warning("A aplicação continuará, mas funcionalidades RAG não funcionarão até o Qdrant estar configurado.")
            # Não fazer raise - permitir que a aplicação inicie mesmo sem Qdrant
            # O erro será capturado quando tentar usar o Qdrant
    
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
                
                if "titulo_palestra" in filters:
                    conditions.append(
                        FieldCondition(
                            key="titulo_palestra",
                            match=MatchValue(value=filters["titulo_palestra"])
                        )
                    )
                
                if "dia" in filters:
                    conditions.append(
                        FieldCondition(
                            key="dia",
                            match=MatchValue(value=filters["dia"])
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

