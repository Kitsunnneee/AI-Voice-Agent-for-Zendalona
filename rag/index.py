from llama_index.core import VectorStoreIndex, load_index_from_storage
from llama_index.core import Settings
from llama_index.core.storage import StorageContext
import os
import config
from rag.document_processor import DocumentProcessor
from rag.embeddings import EmbeddingProvider

class IndexManager:

    @staticmethod
    def create_index(documents=None, embedding_model=None, storage_dir=None):
        storage_dir = storage_dir or config.STORAGE_DIR
        
        if documents is None:
            documents = DocumentProcessor.load_documents()
            documents = DocumentProcessor.preprocess_documents(documents)
        
        if embedding_model is None:
            embedding_model = EmbeddingProvider.get_embedding_model()
        
        index = VectorStoreIndex.from_documents(
            documents,
            embed_model=embedding_model,
            show_progress=True
        )
        
        os.makedirs(storage_dir, exist_ok=True)
        
        index.storage_context.persist(persist_dir=storage_dir)
        
        print(f"Index created and persisted to {storage_dir}")
        
        return index
    
    @staticmethod
    def load_index(storage_dir=None, embedding_model=None):
        storage_dir = storage_dir or config.STORAGE_DIR
        
        if not os.path.exists(storage_dir):
            raise ValueError(f"Index storage directory {storage_dir} does not exist")
        
        if embedding_model is None:
            embedding_model = EmbeddingProvider.get_embedding_model()
        
        Settings.embed_model = embedding_model
        
        storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
        
        index = load_index_from_storage(storage_context)
        
        print(f"Index loaded from {storage_dir}")
        
        return index
