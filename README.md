# SalesCode.ai

Smart voice interruption handler for LiveKit agents that distinguishes between filler words and genuine interruptions.

## Features

- **Filler Word Detection**: Ignores common fillers like "umm", "uh", "hmm" while the agent is speaking
- **Smart Interruption**: Allows real commands like "stop" or "wait" to interrupt the agent
- **Real-time Processing**: Uses STT transcription to intelligently filter interruptions
- **Customizable**: Easy to add more filler words or adjust behavior

## Setup

1. Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
cp .env.example .env
```

3. Add your credentials to `.env`:
```
LIVEKIT_URL=your-livekit-url
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret
OPENAI_API_KEY=your-openai-key
```

## Usage

Run the agent:
```bash
python agent.py dev
```

## How It Works

1. Agent starts speaking
2. User input is transcribed via STT
3. `InterruptionHandler` checks if input contains only filler words
4. If fillers only: Agent continues speaking
5. If valid speech: Agent stops and responds

## Requirements

- Python 3.10+
- LiveKit Agents SDK 1.3+
- OpenAI API access