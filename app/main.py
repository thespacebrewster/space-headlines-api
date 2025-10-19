from fastapi import FastAPI
from app.feed import fetch_headlines

app = FastAPI(title="Space Headlines API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/headlines")
def get_headlines(limit: int = 20):
    """Get space news headlines from multiple sources"""
    headlines = fetch_headlines(limit=limit)
    return {
        "count": len(headlines),
        "headlines": headlines
    }


