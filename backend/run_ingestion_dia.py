#!/usr/bin/env python3
"""
Script para executar o pipeline de ingestão de PDFs por dia.
Uso: python run_ingestion_dia.py dia1
     python run_ingestion_dia.py dia2
     python run_ingestion_dia.py all
"""
import sys
import os
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

from ingestion.ingestion_pipeline import IngestionPipeline
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def process_dia(dia: str):
    """Processar PDFs de um dia específico"""
    pdf_directory = f"../data/pdfs/{dia}"
    
    if not os.path.exists(pdf_directory):
        logger.error(f"Diretório {pdf_directory} não encontrado!")
        return False
    
    pdf_files = list(Path(pdf_directory).glob("*.pdf"))
    
    if not pdf_files:
        logger.warning(f"Nenhum PDF encontrado em {pdf_directory}")
        return False
    
    logger.info("=" * 60)
    logger.info(f"Processando PDFs do {dia.upper()}")
    logger.info(f"Encontrados {len(pdf_files)} arquivos PDF")
    logger.info("=" * 60)
    
    try:
        pipeline = IngestionPipeline(pdf_directory=pdf_directory)
        pipeline.run()
        logger.info(f"✓ Processamento do {dia.upper()} concluído!")
        return True
    except Exception as e:
        logger.error(f"Erro ao processar {dia}: {str(e)}", exc_info=True)
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python run_ingestion_dia.py <dia1|dia2|all>")
        sys.exit(1)
    
    dia_arg = sys.argv[1].lower()
    
    if dia_arg == "all":
        logger.info("Processando todos os dias...")
        success1 = process_dia("dia1")
        success2 = process_dia("dia2")
        if success1 and success2:
            logger.info("✓ Todos os dias processados com sucesso!")
        else:
            logger.error("Alguns dias falharam no processamento")
            sys.exit(1)
    elif dia_arg in ["dia1", "dia2"]:
        success = process_dia(dia_arg)
        if not success:
            sys.exit(1)
    else:
        logger.error(f"Dia inválido: {dia_arg}. Use 'dia1', 'dia2' ou 'all'")
        sys.exit(1)

