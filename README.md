# Abot

Abot is a personal AI operating system designed to help a-boy (ahmeng) become a DeepUse AI Master.

## Features

- Modular skill system
- Pluggable LLM models (Ollama, OpenAI, NanoChat)
- Memory system for learning
- Daily learning loop
- FastAPI-based brain API

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   uvicorn app:app --reload
   ```

3. For Ollama integration, ensure Ollama is running locally.

## API Endpoints

- `GET /run/{skill}`: Execute a skill
- `GET /learn`: Trigger daily learning

## Project Structure

- `app.py`: Main FastAPI application
- `brain/`: Core brain modules (memory, router, learning)
- `models/`: LLM client implementations
- `skills/`: Skill modules
- `data/`: Data storage (memory.json)
- `identity.md`: Abot's identity and mission