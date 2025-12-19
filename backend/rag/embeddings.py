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
        
        self.client = OpenAI(api_key=self.openai_api_key)
        self.model = "text-embedding-ada-002"
        self.dimension = 1536
        
        logger.info("EmbeddingGenerator inicializado")
    
    def generate(self, text: str) -> List[float]:
        """
        Gerar embedding para um texto.
        
        Args:
            text: Texto para gerar embedding
        
        Returns:
            Lista de floats representando o embedding
        """
        try:
            response = self.client.embeddings.create(
                model=self.model,
                input=text
            )
            
            return response.data[0].embedding
        
        except Exception as e:
            logger.error(f"Erro ao gerar embedding: {str(e)}")
            raise

