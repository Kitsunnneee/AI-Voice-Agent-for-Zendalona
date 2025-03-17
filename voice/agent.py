import asyncio
from livekit.agents import llm
from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import silero
import config
from rag.index import IndexManager
from rag.retreiver import RetrieverManager
from voice.stt import SpeechToText
from voice.tts import TextToSpeech
from voice.llm import LanguageModel

class VoiceAssistantAgent:
    def __init__(self):
        config.check_environment()
        
        self.stt = SpeechToText.get_stt()
        self.tts = TextToSpeech.get_tts()
        self.language_model = LanguageModel.get_llm()
        
        self.index = None
        self.query_engine = None
        self._initialize_rag()
        
        self.chat_ctx = llm.ChatContext().append(
            role="system",
            text="You are a helpful voice assistant powered by RAG technology. You have access to a knowledge base and can answer questions based on that information. Keep your responses concise and conversational."
        )
        
        self.vad = silero.VAD.load()
        
        self.agent = VoicePipelineAgent(
            vad=self.vad,
            stt=self.stt,
            llm=self.language_model,
            tts=self.tts,
            chat_ctx=self.chat_ctx,
            allow_interruptions=True,
            interrupt_speech_duration=0.5,
            interrupt_min_words=0,
            min_endpointing_delay=0.5,
            before_llm_cb=self._before_llm_callback
        )
        
        self._setup_event_handlers()
        
        print("Voice assistant agent initialized and ready")
    
    def _initialize_rag(self):
        try:
            self.index = IndexManager.load_index()
        except (ValueError, FileNotFoundError) as e:
            print(f"Error loading index: {e}")
            print("Creating new index...")
            
            import os
            os.makedirs(config.STORAGE_DIR, exist_ok=True)
            
            self.index = IndexManager.create_index()
        
        self.query_engine = RetrieverManager.get_query_engine(
            self.index,
            llm=self.language_model
        )
    
    def _setup_event_handlers(self):
        @self.agent.on("user_speech_committed")
        def on_user_speech_committed(message):
            content = message.content
            if isinstance(content, list):
                content = next((item for item in content if isinstance(item, str)), "")
            print(f"User said: {content}")
        
        @self.agent.on("agent_speech_committed")
        def on_agent_speech_committed(message):
            content = message.content
            if isinstance(content, list):
                content = next((item for item in content if isinstance(item, str)), "")
            print(f"Agent said: {content}")
        
        @self.agent.on("user_started_speaking")
        def on_user_started_speaking():
            print("User started speaking")
        
        @self.agent.on("user_stopped_speaking")
        def on_user_stopped_speaking():
            print("User stopped speaking")
            
    async def _before_llm_callback(self, agent, context):
        last_user_message = None
        for message in context.messages:
            if message.role == "user":
                last_user_message = message
        
        if last_user_message:
            if isinstance(last_user_message.content, str):
                query_text = last_user_message.content
            elif isinstance(last_user_message.content, list):
                query_text = next((item for item in last_user_message.content if isinstance(item, str)), "")
            else:
                query_text = ""
            
            if query_text:
                response = self.query_engine.query(query_text)
                
                context.append(
                    role="system",
                    text=f"Relevant information from knowledge base: {str(response)}"
                )
        
        return None
    
    def start(self, room, participant):
        self.agent.start(room, participant)
        
    async def say(self, text, allow_interruptions=True):
        await self.agent.say(text, allow_interruptions=allow_interruptions)
