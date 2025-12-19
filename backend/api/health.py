"""
Health check endpoints
"""
from fastapi import APIRouter
from pydantic import BaseModel

health_router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    service: str


@health_router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(status="healthy", service="Product Camp 2025 RAG API")

