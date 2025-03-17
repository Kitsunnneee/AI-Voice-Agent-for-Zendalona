from livekit.plugins.cartesia import tts as cartesia_tts
import config

class TextToSpeech:
    @staticmethod
    def get_tts():

        if not config.CARTESIA_API_KEY:
            raise ValueError("CARTESIA_API_KEY is not set in environment variables")
        

        synthesizer = cartesia_tts.TTS(
            model=config.TTS_MODEL,
            voice=config.TTS_VOICE,
            speed=config.TTS_SPEED,
            emotion=config.TTS_EMOTIONS
        )
        
        print("Text-to-speech service initialized")
        
        return synthesizer
