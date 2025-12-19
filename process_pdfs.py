#!/usr/bin/env python3
"""
Script para processar PDFs organizados por dia (Dia1 e Dia2)
"""
import sys
import os
from pathlib import Path

# Adicionar backend ao path
sys.path.insert(0, str(Path(__file__).parent / "backend"))

from ingestion.ingestion_pipeline import IngestionPipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_dia(dia: str):
    """
    Processar PDFs de um dia específico.
    
    Args:
        dia: 'dia1' ou 'dia2'
    """
    pdf_directory = f"data/pdfs/{dia}"
    
    if not os.path.exists(pdf_directory):
        logger.error(f"Diretório {pdf_directory} não encontrado!")
        return
    
    pdf_files = list(Path(pdf_directory).glob("*.pdf"))
    
    if not pdf_files:
        logger.warning(f"Nenhum PDF encontrado em {pdf_directory}")
        return
    
    logger.info(f"=" * 60)
    logger.info(f"Processando PDFs do {dia.upper()}")
    logger.info(f"Encontrados {len(pdf_files)} arquivos PDF")
    logger.info(f"=" * 60)
    
    pipeline = IngestionPipeline(pdf_directory=pdf_directory)
    pipeline.run()
    
    logger.info(f"✓ Processamento do {dia.upper()} concluído!")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Processar PDFs do Product Camp 2025")
    parser.add_argument(
        "dia",
        choices=["dia1", "dia2", "all"],
        help="Dia a processar: dia1, dia2 ou all (todos)"
    )
    
    args = parser.parse_args()
    
    if args.dia == "all":
        logger.info("Processando todos os dias...")
        process_dia("dia1")
        process_dia("dia2")
    else:
        process_dia(args.dia)

