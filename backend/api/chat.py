"""
Chat endpoint para consultas RAG
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
import logging

from rag.rag_engine import RAGEngine

logger = logging.getLogger(__name__)

chat_router = APIRouter()


class ChatRequest(BaseModel):
    question: str
    filters: Optional[Dict[str, str]] = None


class Source(BaseModel):
    titulo_palestra: str
    palestrante: str
    tipo: str
    tema: Optional[str] = None
    pagina_ou_slide: Optional[str] = None
    score: float


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
    query: str


# Inicializar RAG Engine
rag_engine = RAGEngine()


@chat_router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Endpoint principal para fazer perguntas sobre as palestras.
    
    Recebe uma pergunta e filtros opcionais, retorna resposta
    contextualizada com citações das fontes.
    """
    try:
        if not request.question or not request.question.strip():
            raise HTTPException(
                status_code=400,
                detail="A pergunta não pode estar vazia"
            )
        
        logger.info(f"Recebida pergunta: {request.question}")
        logger.info(f"Filtros aplicados: {request.filters}")
        
        # Processar pergunta através do RAG Engine
        result = await rag_engine.query(
            question=request.question,
            filters=request.filters or {}
        )
        
        logger.info(f"Resposta gerada com {len(result['sources'])} fontes")
        
        return ChatResponse(
            answer=result["answer"],
            sources=[
                Source(
                    titulo_palestra=src["titulo_palestra"],
                    palestrante=src["palestrante"],
                    tipo=src["tipo"],
                    tema=src.get("tema"),
                    pagina_ou_slide=src.get("pagina_ou_slide"),
                    score=src.get("score", 0.0)
                )
                for src in result["sources"]
            ],
            query=request.question
        )
    
    except Exception as e:
        logger.error(f"Erro ao processar pergunta: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar pergunta: {str(e)}"
        )

