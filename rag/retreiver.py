from llama_index.core.indices.vector_store.retrievers.retriever import VectorIndexRetriever
from llama_index.core.query_engine.retriever_query_engine import RetrieverQueryEngine
from typing import Optional
import config

class RetrieverManager:
    @staticmethod
    def get_retriever(index, similarity_top_k=None):

        similarity_top_k = similarity_top_k or config.TOP_K_RETRIEVAL
        
        retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=similarity_top_k
        )
        
        return retriever
    
    @staticmethod
    def get_query_engine(index=None, retriever=None, similarity_top_k=None, llm=None):
        if retriever is None:
            if index is None:
                raise ValueError("Either index or retriever must be provided")
                
            retriever = RetrieverManager.get_retriever(
                index, 
                similarity_top_k=similarity_top_k
            )
        

        query_engine = RetrieverQueryEngine.from_args(
            retriever=retriever,
            response_mode="compact" 
        )
        
        return query_engine
