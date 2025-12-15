
import chromadb
from chromadb.config import Settings
#from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from typing import Dict,Any,List

class VectorStore:
    """Manages ChromaDB vector store for product knowledge base"""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(anonymized_telemetry=False)
        )
        
        self.collection = self.client.get_or_create_collection(
            name="health_products",
            embedding_function=None,
            metadata={"hnsw:space": "cosine"}
        )