from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Vidyanvesha OSM AI",
    description="AI Agent service for Vidyanvesha OSM",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "osm-ai-evaluator"}