import os
from dotenv import load_dotenv


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
LIVEKIT_URL = os.getenv("LIVEKIT_URL")


LLM_MODEL = "llama3-70b-8192"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TTS_MODEL = "sonic-english"
TTS_VOICE = "c2ac25f9-ecc4-4f56-9095-651354df60c0"
TTS_SPEED = 0.9
TTS_EMOTIONS = ["curiosity:high", "positivity:high"]

TOP_K_RETRIEVAL = 3
DATA_DIR = "data"
STORAGE_DIR = "storage"


def check_environment():
    required_vars = ["GROQ_API_KEY", "CARTESIA_API_KEY", "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET", "LIVEKIT_URL"]
    missing_vars = [var for var in required_vars if not globals().get(var)]
    
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return True
