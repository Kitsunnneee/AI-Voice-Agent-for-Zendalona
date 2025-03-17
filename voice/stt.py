from livekit.plugins.openai import stt
import config

class SpeechToText:

    @staticmethod
    def get_stt():
        if not config.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set in environment variables")
        
        transcriber = stt.STT.with_groq(
            model="whisper-large-v3",
            language="en"
        )
        
        print("Speech-to-text service initialized with Groq")
        
        return transcriber
