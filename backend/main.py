"""
FastAPI Backend para Product Camp 2025 RAG System
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, List
import os
from dotenv import load_dotenv
import logging

from api.chat import chat_router
from api.health import health_router
from api.ingestion import ingestion_router

# Carregar variáveis de ambiente
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Criar aplicação FastAPI
app = FastAPI(
    title="Product Camp 2025 RAG API",
    description="API para consultas sobre palestras do Product Camp 2025",
    version="1.0.0"
)

# Configurar CORS
cors_origins_str = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001")
cors_origins = [origin.strip() for origin in cors_origins_str.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(chat_router, prefix="/api", tags=["chat"])
app.include_router(health_router, prefix="/api", tags=["health"])
app.include_router(ingestion_router, prefix="/api", tags=["ingestion"])


@app.get("/")
async def root():
    """Endpoint raiz"""
    return {
        "message": "Product Camp 2025 RAG API",
        "version": "1.0.0",
        "status": "running"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

