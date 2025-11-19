import logging
from livekit.agents import UserInputTranscribedEvent, voice
from config import IGNORED_FILLERS

logger = logging.getLogger("handler")

class InterruptionHandler:
    def __init__(self, session: voice.AgentSession):
        self.session = session
        self.is_speaking = False
        self.setup()

    def setup(self):
        self.session.on("user_input_transcribed", self.on_transcription)
        self.session.on("speech_created", self.on_speech_start)
        self.session.on("agent_state_changed", self.on_state_change)

    def on_speech_start(self, event):
        self.is_speaking = True

    def on_state_change(self, event):
        if event.agent_state == "listening":
            self.is_speaking = False

    def on_transcription(self, event: UserInputTranscribedEvent):
        if not self.is_speaking:
            return

        text = event.text.strip()
        if not text:
            return

        clean = ''.join(c for c in text if c.isalnum() or c.isspace()).lower()
        words = clean.split()
        
        if not words:
            return

        if all(w in IGNORED_FILLERS for w in words):
            logger.info(f"Ignored: {text}")
            self.session.clear_user_turn()
        else:
            logger.info(f"Valid: {text}")