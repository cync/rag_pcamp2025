"""
PDF Processor - Extração e processamento de PDFs
"""
import os
import logging
from typing import List, Dict, Optional
import pdfplumber
from pathlib import Path

logger = logging.getLogger(__name__)


class PDFProcessor:
    """
    Processador de PDFs para extrair texto e metadados.
    
    Responsável por:
    - Ler PDFs de um diretório
    - Extrair texto por página ou slide
    - Identificar estrutura do documento
    """
    
    def __init__(self, pdf_directory: str = "data/pdfs"):
        """
        Inicializar processador.
        
        Args:
            pdf_directory: Caminho para diretório com PDFs
        """
        self.pdf_directory = Path(pdf_directory)
        if not self.pdf_directory.exists():
            logger.warning(f"Diretório {pdf_directory} não existe. Criando...")
            self.pdf_directory.mkdir(parents=True, exist_ok=True)
    
    def extract_text_from_pdf(self, pdf_path: str) -> List[Dict[str, any]]:
        """
        Extrair texto de um PDF, dividido por página.
        
        Args:
            pdf_path: Caminho para o arquivo PDF
        
        Returns:
            Lista de dicionários com texto e número da página
        """
        pages = []
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    
                    if text and text.strip():
                        pages.append({
                            "text": text.strip(),
                            "page_number": page_num,
                            "total_pages": len(pdf.pages)
                        })
            
            logger.info(f"Extraídos {len(pages)} páginas de {pdf_path}")
            return pages
        
        except Exception as e:
            logger.error(f"Erro ao processar PDF {pdf_path}: {str(e)}")
            return []
    
    def get_all_pdfs(self) -> List[str]:
        """
        Listar todos os PDFs no diretório e subdiretórios.
        
        Returns:
            Lista de caminhos para arquivos PDF
        """
        # Buscar recursivamente em todos os subdiretórios
        pdf_files = list(self.pdf_directory.rglob("*.pdf"))
        logger.info(f"Encontrados {len(pdf_files)} arquivos PDF em {self.pdf_directory}")
        if pdf_files:
            logger.info(f"PDFs encontrados: {[str(p.name) for p in pdf_files[:5]]}...")
        return [str(pdf) for pdf in pdf_files]
    
    def parse_filename_metadata(self, filename: str, pdf_directory = None) -> Dict[str, Optional[str]]:
        """
        Tentar extrair metadados do nome do arquivo e diretório.
        
        Formato esperado (opcional):
        - "Titulo_Palestra_Palestrante_Tipo_Tema.pdf"
        - Ou usar valores padrão
        
        Detecta automaticamente se está em dia1 ou dia2.
        
        Args:
            filename: Nome do arquivo PDF
            pdf_directory: Diretório do PDF (para detectar dia)
        
        Returns:
            Dicionário com metadados
        """
        # Remover extensão
        name = Path(filename).stem
        
        # Detectar dia do diretório
        dia = None
        if pdf_directory:
            # Converter para string se for Path object
            pdf_dir_str = str(pdf_directory)
            if "dia1" in pdf_dir_str.lower():
                dia = "Dia 1"
            elif "dia2" in pdf_dir_str.lower():
                dia = "Dia 2"
        
        # Tentar dividir por underscore ou hífen
        parts = name.replace("_", "-").split("-")
        
        metadata = {
            "titulo_palestra": name,  # Padrão: usar nome completo
            "palestrante": "Desconhecido",
            "tipo": "palestra",  # Padrão
            "tema": None,
            "dia": dia  # Adicionar informação do dia
        }
        
        # Se tiver pelo menos 2 partes, tentar interpretar
        if len(parts) >= 2:
            metadata["titulo_palestra"] = parts[0].strip()
            metadata["palestrante"] = parts[1].strip() if len(parts) > 1 else "Desconhecido"
            
            if len(parts) >= 3:
                tipo = parts[2].strip().lower()
                if tipo in ["keynote", "workshop", "palestra"]:
                    metadata["tipo"] = tipo
            
            if len(parts) >= 4:
                metadata["tema"] = parts[3].strip()
        
        return metadata

