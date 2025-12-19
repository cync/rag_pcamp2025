"""
Endpoint para executar ingestão de PDFs (apenas em produção com autenticação)
"""
from fastapi import APIRouter, HTTPException, Header
from typing import Optional
import os
import logging

logger = logging.getLogger(__name__)

ingestion_router = APIRouter()


@ingestion_router.post("/ingest")
async def run_ingestion(x_api_key: Optional[str] = Header(None)):
    """
    Endpoint para executar ingestão de PDFs.
    
    Requer API key para segurança em produção.
    """
    # Verificar API key
    expected_key = os.getenv("INGESTION_API_KEY")
    
    if not expected_key:
        # Se não configurado, permitir apenas em desenvolvimento
        if os.getenv("ENVIRONMENT") == "production":
            raise HTTPException(
                status_code=403,
                detail="Ingestion API key not configured"
            )
    else:
        # Verificar se a chave fornecida está correta
        if x_api_key != expected_key:
            raise HTTPException(
                status_code=403,
                detail="Invalid API key"
            )
    
    try:
        from ingestion.ingestion_pipeline import IngestionPipeline
        
        logger.info("Iniciando ingestão via API endpoint")
        pipeline = IngestionPipeline()
        pipeline.run()
        
        return {
            "status": "success",
            "message": "Ingestion completed successfully"
        }
    except Exception as e:
        logger.error(f"Erro na ingestão: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao executar ingestão: {str(e)}"
        )

