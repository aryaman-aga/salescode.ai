import logging
import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, voice
from livekit.plugins import openai, silero
from interruption_handler import InterruptionHandler

load_dotenv()
logger = logging.getLogger("agent")

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    agent = voice.Agent(
        instructions="You are a helpful assistant. Speak naturally and concisely.",
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        allow_interruptions=False,
    )

    session = await agent.start(ctx.room)
    handler = InterruptionHandler(session)
    
    await asyncio.sleep(1)
    await session.say("Hi! I'm your assistant. Try interrupting me with 'umm' or 'stop' to see what happens.")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))