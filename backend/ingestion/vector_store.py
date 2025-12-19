"""
Vector Store para ingestão - Extensão do vector_store principal
"""
from rag.vector_store import VectorStore as BaseVectorStore


class VectorStore(BaseVectorStore):
    """
    Extensão do VectorStore para uso no pipeline de ingestão.
    Adiciona métodos específicos para inserção de dados.
    """
    pass

