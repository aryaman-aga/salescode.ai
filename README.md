LiveKit Voice Interruption Handling (SalesCode Challenge)

This repository contains a solution for intelligent voice interruption handling. It extends the standard LiveKit VoicePipelineAgent to distinguish between "filler words" (which are ignored) and "genuine interruptions" (which stop the agent).

What Changed

I implemented a custom extension layer SmartInterruptionHandler that sits on top of the LiveKit Agent.

Logic Added: instead of relying solely on VAD (Voice Activity Detection) for interruptions, I utilize the STT (Speech-to-Text) stream.

New Modules: - interruption_handler.py: Contains the logic to filter transcription_received events.

config.py: Centralized list of IGNORED_FILLERS and confidence thresholds.

Workflow:

Agent speaks.

User makes a sound.

interruption_handler captures the transcription.

If the text matches the ignore list (e.g., "umm", "hmm"), the agent continues.

If the text is valid (e.g., "wait", "stop"), agent.interrupt() is triggered manually.

What Works

Filler Suppression: The agent successfully ignores "uh", "umm", "hmm" while speaking.

Valid Interruptions: Commands like "Stop" or "Wait" immediately halt the TTS.

Silence Handling: If the agent is silent, "umm" is processed as normal user speech (as per requirements).

Noise Filtering: Low-confidence transcriptions (background murmur) are ignored.

Steps to Test

Setup Environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Configure Keys:
Create a .env file:

LIVEKIT_URL=...
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
OPENAI_API_KEY=...


Run the Agent:

python agent.py dev


Verification:

Connect to the playground/frontend.

Let the agent start its monologue.

Say "Umm" or "Hmm" clearly. Expected: Agent continues talking.

Say "Stop" or "Wait a second". Expected: Agent stops talking immediately.

Environment Details

Python: 3.10+

SDK: livekit-agents>=0.8.0

Plugins: OpenAI (STT/LLM/TTS), Silero (VAD)