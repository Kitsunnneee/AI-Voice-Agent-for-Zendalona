from livekit.plugins.openai import llm
import config

class LanguageModel:
    @staticmethod
    def get_llm():

        if not config.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set in environment variables")
            
        language_model = llm.LLM.with_groq(
            model=config.LLM_MODEL,
            temperature=0.7
        )
        
        print(f"Language model initialized with Groq: {config.LLM_MODEL}")
        
        return language_model
