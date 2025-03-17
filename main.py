import asyncio
import os
import sys
from dotenv import load_dotenv
from voice.agent import VoiceAssistantAgent
from rag.index import IndexManager
from rag.document_processor import DocumentProcessor
from utils.helpers import create_directory_if_not_exists
import config
from livekit import rtc
from livekit.agents.cli import run_app
from livekit.agents import JobContext, WorkerOptions, AutoSubscribe

from llama_index.core import Settings
from llama_index.llms.groq import Groq

load_dotenv()

async def entrypoint(ctx: JobContext):
    """Entry point for the agent worker."""
    create_directory_if_not_exists(config.DATA_DIR)
    create_directory_if_not_exists(config.STORAGE_DIR)
    
    groq_llm = Groq(
        api_key=config.GROQ_API_KEY,
        model=config.LLM_MODEL
    )
    Settings.llm = groq_llm
    
    agent = VoiceAssistantAgent()
    
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    
    participant = await ctx.wait_for_participant()
    print(f"Participant joined: {participant.identity}")
    
    agent.start(ctx.room, participant)
    

    await agent.say("Hello! I'm your voice assistant. How can I help you today?")
    
    while True:
        await asyncio.sleep(1)

def main():

    create_directory_if_not_exists(config.DATA_DIR)
    create_directory_if_not_exists(config.STORAGE_DIR)
    

    try:
        config.check_environment()
    except EnvironmentError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    run_app(WorkerOptions(entrypoint_fnc=entrypoint))

if __name__ == "__main__":
    main()
