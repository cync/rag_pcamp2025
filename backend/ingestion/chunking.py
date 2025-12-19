"""
Chunking - Divisão de texto em chunks semânticos
"""
import logging
from typing import List, Dict
import re

logger = logging.getLogger(__name__)


class ChunkingStrategy:
    """
    Estratégias para dividir texto em chunks.
    
    Preferencialmente por slide ou seção, mantendo
    contexto semântico.
    """
    
    @staticmethod
    def chunk_by_slides(text: str, page_number: int) -> List[Dict[str, any]]:
        """
        Dividir texto tentando identificar slides.
        
        Slides geralmente são separados por:
        - Quebras de linha duplas
        - Números de slide
        - Títulos em maiúsculas
        
        Args:
            text: Texto da página
            page_number: Número da página
        
        Returns:
            Lista de chunks com texto e metadados
        """
        chunks = []
        
        # Tentar dividir por quebras de linha duplas
        sections = re.split(r'\n\s*\n+', text)
        
        for i, section in enumerate(sections, 1):
            section = section.strip()
            
            if len(section) < 50:  # Ignorar seções muito pequenas
                continue
            
            # Se a seção for muito grande (>2000 chars), dividir mais
            if len(section) > 2000:
                sub_chunks = ChunkingStrategy._split_large_section(section)
                for j, sub_chunk in enumerate(sub_chunks, 1):
                    chunks.append({
                        "text": sub_chunk,
                        "slide_number": f"{page_number}-{i}-{j}",
                        "page_number": page_number
                    })
            else:
                chunks.append({
                    "text": section,
                    "slide_number": f"{page_number}-{i}",
                    "page_number": page_number
                })
        
        # Se não encontrou divisões claras, usar a página inteira
        if not chunks:
            chunks.append({
                "text": text,
                "slide_number": str(page_number),
                "page_number": page_number
            })
        
        return chunks
    
    @staticmethod
    def _split_large_section(text: str, max_size: int = 1500, overlap: int = 200) -> List[str]:
        """
        Dividir seção grande em chunks menores com overlap.
        
        Args:
            text: Texto para dividir
            max_size: Tamanho máximo do chunk
            overlap: Sobreposição entre chunks
        
        Returns:
            Lista de chunks
        """
        chunks = []
        words = text.split()
        current_chunk = []
        current_size = 0
        
        for word in words:
            word_size = len(word) + 1  # +1 para espaço
            
            if current_size + word_size > max_size and current_chunk:
                # Finalizar chunk atual
                chunks.append(" ".join(current_chunk))
                
                # Começar novo chunk com overlap
                overlap_words = current_chunk[-overlap:] if len(current_chunk) > overlap else current_chunk
                current_chunk = overlap_words + [word]
                current_size = sum(len(w) + 1 for w in current_chunk)
            else:
                current_chunk.append(word)
                current_size += word_size
        
        # Adicionar último chunk
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        return chunks
    
    @staticmethod
    def chunk_by_pages(pages: List[Dict]) -> List[Dict[str, any]]:
        """
        Dividir por páginas (fallback simples).
        
        Args:
            pages: Lista de páginas com texto
        
        Returns:
            Lista de chunks
        """
        chunks = []
        
        for page in pages:
            text = page["text"]
            page_num = page["page_number"]
            
            # Se página muito grande, dividir
            if len(text) > 2000:
                sub_chunks = ChunkingStrategy._split_large_section(text)
                for i, sub_chunk in enumerate(sub_chunks, 1):
                    chunks.append({
                        "text": sub_chunk,
                        "slide_number": f"{page_num}-{i}",
                        "page_number": page_num
                    })
            else:
                chunks.append({
                    "text": text,
                    "slide_number": str(page_num),
                    "page_number": page_num
                })
        
        return chunks

