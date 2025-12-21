"""
Ingestion Pipeline - Pipeline completo de ingestão de PDFs
"""
import os
import logging
from typing import List, Dict
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

from ingestion.pdf_processor import PDFProcessor
from ingestion.chunking import ChunkingStrategy
from rag.vector_store import VectorStore
from rag.embeddings import EmbeddingGenerator

# Carregar variáveis de ambiente
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class IngestionPipeline:
    """
    Pipeline completo de ingestão.
    
    Fluxo:
    1. Ler PDFs do diretório
    2. Extrair texto
    3. Dividir em chunks
    4. Gerar embeddings
    5. Armazenar no Qdrant
    """
    
    def __init__(self, pdf_directory: str = "data/pdfs"):
        """
        Inicializar pipeline.
        
        Args:
            pdf_directory: Diretório com PDFs
        """
        self.pdf_processor = PDFProcessor(pdf_directory)
        self.vector_store = VectorStore()
        self.embedding_generator = EmbeddingGenerator()
        
        # Criar collection se não existir
        self.vector_store.create_collection_if_not_exists(vector_size=1536)
    
    def run(self):
        """Executar pipeline completo"""
        logger.info("=" * 60)
        logger.info("Iniciando pipeline de ingestão de PDFs")
        logger.info("=" * 60)
        
        # 1. Listar PDFs
        pdf_files = self.pdf_processor.get_all_pdfs()
        
        if not pdf_files:
            logger.warning("Nenhum PDF encontrado no diretório!")
            return
        
        total_chunks = 0
        
        # 2. Processar cada PDF
        for pdf_path in pdf_files:
            try:
                logger.info(f"\nProcessando: {pdf_path}")
                
                # Extrair metadados do nome do arquivo
                metadata = self.pdf_processor.parse_filename_metadata(
                    pdf_path, 
                    pdf_directory=str(self.pdf_processor.pdf_directory)
                )
                metadata["fonte"] = "Product Camp 2025"
                
                # Extrair texto
                pages = self.pdf_processor.extract_text_from_pdf(pdf_path)
                
                if not pages:
                    logger.warning(f"Nenhum texto extraído de {pdf_path}")
                    continue
                
                # Dividir em chunks
                all_chunks = []
                for page in pages:
                    chunks = ChunkingStrategy.chunk_by_slides(
                        page["text"],
                        page["page_number"]
                    )
                    all_chunks.extend(chunks)
                
                logger.info(f"  → {len(all_chunks)} chunks criados")
                
                # 3. Processar cada chunk
                for chunk_idx, chunk in enumerate(all_chunks, 1):
                    try:
                        # Gerar embedding (com retry automático)
                        embedding = self.embedding_generator.generate(chunk["text"], max_retries=5)
                        
                        # Preparar metadados completos
                        chunk_metadata = {
                            **metadata,
                            "pagina_ou_slide": chunk.get("slide_number", str(chunk["page_number"]))
                        }
                        
                        # Armazenar no Qdrant
                        # Metadados no nível raiz do payload para facilitar filtros
                        self.vector_store.client.upsert(
                            collection_name=self.vector_store.collection_name,
                            points=[{
                                "id": self._generate_point_id(pdf_path, chunk_idx),
                                "vector": embedding,
                                "payload": {
                                    "text": chunk["text"],
                                    "titulo_palestra": chunk_metadata["titulo_palestra"],
                                    "palestrante": chunk_metadata["palestrante"],
                                    "tipo": chunk_metadata["tipo"],
                                    "tema": chunk_metadata.get("tema"),
                                    "pagina_ou_slide": chunk_metadata["pagina_ou_slide"],
                                    "fonte": chunk_metadata.get("fonte", "Product Camp 2025")
                                }
                            }]
                        )
                        
                        total_chunks += 1
                        
                        if chunk_idx % 10 == 0:
                            logger.debug(f"  → Processados {chunk_idx}/{len(all_chunks)} chunks")
                    
                    except Exception as e:
                        logger.error(f"Erro ao processar chunk {chunk_idx}: {str(e)}")
                        continue
                
                logger.info(f"✓ {pdf_path} processado com sucesso")
            
            except Exception as e:
                logger.error(f"Erro ao processar {pdf_path}: {str(e)}", exc_info=True)
                continue
        
        logger.info("\n" + "=" * 60)
        logger.info(f"Ingestão concluída! Total de chunks: {total_chunks}")
        logger.info("=" * 60)
    
    def _generate_point_id(self, pdf_path: str, chunk_idx: int) -> int:
        """
        Gerar ID único para um chunk.
        
        Args:
            pdf_path: Caminho do PDF
            chunk_idx: Índice do chunk
        
        Returns:
            ID único (hash simples)
        """
        import hashlib
        unique_string = f"{pdf_path}_{chunk_idx}"
        return int(hashlib.md5(unique_string.encode()).hexdigest()[:8], 16)


if __name__ == "__main__":
    # Executar pipeline
    pipeline = IngestionPipeline()
    pipeline.run()

