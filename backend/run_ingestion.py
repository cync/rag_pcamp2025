#!/usr/bin/env python3
"""
Script para executar o pipeline de ingestão de PDFs.
"""
import sys
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

from ingestion.ingestion_pipeline import IngestionPipeline

if __name__ == "__main__":
    pipeline = IngestionPipeline()
    pipeline.run()

