from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import config

class EmbeddingProvider:
    @staticmethod
    def get_embedding_model(model_name: str = None):
        model_name = model_name or config.EMBEDDING_MODEL
        
        print(f"Initializing embedding model: {model_name}")
        embed_model = HuggingFaceEmbedding(model_name=model_name)
        
        return embed_model
