# vidyavensha_osm_ai_evaluator# Vidyanvesha OSM AI Evaluator

AI Agent microservice built with FastAPI + LangGraph for the Vidyanvesha OSM (Onscreen Marking) system.

## Tech Stack
- FastAPI
- LangGraph
- LangChain + Groq (LLM)
- Python 3.11+

## Setup
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

## Running
```bash
uvicorn app.main:app --reload
```

## Environment Variables
Create a `.env` file with:
```
GROQ_API_KEY=your_key_here
OSM_BASE_URL=http://localhost:8000
```