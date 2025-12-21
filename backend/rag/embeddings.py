"""
Embedding Generator - Geração de embeddings para queries
"""
import os
import logging
from typing import List
from openai import OpenAI

logger = logging.getLogger(__name__)


class EmbeddingGenerator:
    """
    Gerador de embeddings usando OpenAI.
    
    Usa o modelo text-embedding-ada-002 para gerar
    embeddings de 1536 dimensões.
    """
    
    def __init__(self):
        """Inicializar gerador de embeddings"""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY não encontrada nas variáveis de ambiente")
        
        # Configurar cliente com timeout maior e retry
        import httpx
        self.client = OpenAI(
            api_key=self.openai_api_key,
            timeout=httpx.Timeout(60.0, connect=10.0),  # 60s total, 10s para conectar
            max_retries=3
        )
        self.model = "text-embedding-ada-002"
        self.dimension = 1536
        
        logger.info("EmbeddingGenerator inicializado")
    
    def generate(self, text: str, max_retries: int = 5, retry_interval: int = 600) -> List[float]:
        """
        Gerar embedding para um texto.
        
        Args:
            text: Texto para gerar embedding
            max_retries: Número máximo de tentativas
            retry_interval: Intervalo em segundos entre tentativas (padrão: 600s = 10 minutos)
                           Use valores menores (30-60s) para requisições HTTP síncronas
        
        Returns:
            Lista de floats representando o embedding
        """
        import time
        from openai import APIError, APIConnectionError
        
        for attempt in range(max_retries):
            try:
                response = self.client.embeddings.create(
                    model=self.model,
                    input=text
                )
                
                return response.data[0].embedding
            
            except (APIConnectionError, APIError) as e:
                if attempt < max_retries - 1:
                    wait_time = retry_interval
                    wait_minutes = wait_time / 60
                    logger.warning(f"Erro de conexão OpenAI (tentativa {attempt + 1}/{max_retries}): {str(e)}. Aguardando {wait_minutes:.1f} minutos...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Erro ao gerar embedding após {max_retries} tentativas: {str(e)}")
                    raise
            except Exception as e:
                logger.error(f"Erro inesperado ao gerar embedding: {str(e)}")
                raise

