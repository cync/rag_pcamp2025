"""
RAG Engine - Motor principal de Retrieval-Augmented Generation
"""
import os
import logging
from typing import Dict, List, Optional
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
import numpy as np

from rag.vector_store import VectorStore
from rag.embeddings import EmbeddingGenerator

logger = logging.getLogger(__name__)


class RAGEngine:
    """
    Engine principal do sistema RAG.
    
    Responsável por:
    1. Buscar chunks relevantes no Qdrant
    2. Construir prompt contextualizado
    3. Chamar OpenAI para gerar resposta
    4. Retornar resposta com fontes citadas
    """
    
    def __init__(self):
        """Inicializar RAG Engine"""
        # Configurações
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY não encontrada nas variáveis de ambiente")
        
        self.openai_client = OpenAI(api_key=self.openai_api_key)
        self.model = "gpt-4-turbo-preview"  # ou "gpt-3.5-turbo" para economia
        self.max_tokens = 1000
        self.temperature = 0.1  # Baixa temperatura para respostas mais precisas
        
        # Inicializar componentes
        self.vector_store = VectorStore()
        self.embedding_generator = EmbeddingGenerator()
        
        logger.info("RAG Engine inicializado com sucesso")
    
    async def query(
        self,
        question: str,
        filters: Optional[Dict[str, str]] = None
    ) -> Dict[str, any]:
        """
        Processar pergunta e retornar resposta contextualizada.
        
        Args:
            question: Pergunta do usuário
            filters: Filtros opcionais (palestrante, tema, tipo)
        
        Returns:
            Dict com 'answer' e 'sources'
        """
        try:
            # 1. Gerar embedding da pergunta
            logger.debug("Gerando embedding da pergunta...")
            question_embedding = self.embedding_generator.generate(question)
            
            # 2. Buscar chunks relevantes no Qdrant
            logger.debug("Buscando chunks relevantes...")
            relevant_chunks = self.vector_store.search(
                query_vector=question_embedding,
                top_k=5,
                filters=filters or {}
            )
            
            if not relevant_chunks:
                return {
                    "answer": "Desculpe, não encontrei informações relevantes sobre essa pergunta nas palestras disponíveis.",
                    "sources": []
                }
            
            # 3. Construir contexto a partir dos chunks
            context = self._build_context(relevant_chunks)
            
            # 4. Construir prompt estruturado
            prompt = self._build_prompt(question, context)
            
            # 5. Chamar OpenAI
            logger.debug("Chamando OpenAI API...")
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            answer = response.choices[0].message.content.strip()
            
            # 6. Extrair fontes únicas
            sources = self._extract_sources(relevant_chunks)
            
            return {
                "answer": answer,
                "sources": sources
            }
        
        except Exception as e:
            logger.error(f"Erro no RAG Engine: {str(e)}", exc_info=True)
            raise
    
    def _build_context(self, chunks: List[Dict]) -> str:
        """Construir contexto formatado a partir dos chunks"""
        context_parts = []
        
        for i, chunk in enumerate(chunks, 1):
            metadata = chunk.get("metadata", {})
            context_parts.append(
                f"[Fonte {i}]\n"
                f"Palestra: {metadata.get('titulo_palestra', 'N/A')}\n"
                f"Palestrante: {metadata.get('palestrante', 'N/A')}\n"
                f"Tipo: {metadata.get('tipo', 'N/A')}\n"
                f"Tema: {metadata.get('tema', 'N/A')}\n"
                f"Página/Slide: {metadata.get('pagina_ou_slide', 'N/A')}\n"
                f"Conteúdo:\n{chunk.get('text', '')}\n"
            )
        
        return "\n---\n".join(context_parts)
    
    def _build_prompt(self, question: str, context: str) -> str:
        """Construir prompt para o LLM"""
        return f"""Com base EXCLUSIVAMENTE nas informações fornecidas abaixo, responda à seguinte pergunta.

CONTEXTO DAS PALESTRAS:
{context}

PERGUNTA DO USUÁRIO:
{question}

INSTRUÇÕES:
1. Responda APENAS com base nas informações do contexto fornecido
2. Se a informação não estiver no contexto, diga claramente que não encontrou essa informação
3. Sempre cite a palestra e o palestrante quando mencionar informações específicas
4. Seja claro, objetivo e amigável
5. Se possível, compare ou relacione informações de diferentes palestras quando relevante
6. NÃO invente ou assuma informações que não estão no contexto"""
    
    def _get_system_prompt(self) -> str:
        """Prompt do sistema para o LLM"""
        return """Você é um assistente especializado em ajudar participantes do Product Camp 2025 a encontrar informações sobre as palestras do evento.

Sua função é:
- Responder perguntas com base EXCLUSIVAMENTE no conteúdo das palestras fornecidas
- Sempre citar a origem das informações (palestra e palestrante)
- Ser preciso e evitar qualquer alucinação ou invenção de conteúdo
- Ser útil, claro e profissional

IMPORTANTE: Se você não tiver informações suficientes no contexto fornecido, seja honesto e diga que não encontrou essa informação específica."""
    
    def _extract_sources(self, chunks: List[Dict]) -> List[Dict]:
        """Extrair e deduplicar fontes dos chunks"""
        seen = set()
        sources = []
        
        for chunk in chunks:
            metadata = chunk.get("metadata", {})
            source_key = (
                metadata.get("titulo_palestra", ""),
                metadata.get("palestrante", "")
            )
            
            if source_key not in seen:
                seen.add(source_key)
                sources.append({
                    "titulo_palestra": metadata.get("titulo_palestra", "N/A"),
                    "palestrante": metadata.get("palestrante", "N/A"),
                    "tipo": metadata.get("tipo", "N/A"),
                    "tema": metadata.get("tema"),
                    "pagina_ou_slide": metadata.get("pagina_ou_slide"),
                    "score": chunk.get("score", 0.0)
                })
        
        return sources

