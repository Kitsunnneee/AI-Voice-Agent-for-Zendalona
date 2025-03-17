from llama_index.core import SimpleDirectoryReader
from typing import List, Optional
import os
import config

class DocumentProcessor:
    @staticmethod
    def load_documents(directory: str = None, file_paths: List[str] = None):

        directory = directory or config.DATA_DIR
        
        if not os.path.exists(directory) and not file_paths:
            raise ValueError(f"Directory {directory} does not exist and no file paths provided")
        
        reader = SimpleDirectoryReader(
            input_dir=directory if os.path.exists(directory) else None,
            input_files=file_paths
        )
        
        documents = reader.load_data()
        print(f"Loaded {len(documents)} documents")
        
        return documents
    
    @staticmethod
    def preprocess_documents(documents: List):

        for i, doc in enumerate(documents):
            print(f"Document {i}: {len(doc.text)} characters")
        
        return documents
