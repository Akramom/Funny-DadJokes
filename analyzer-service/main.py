from fastapi import FastAPI, Request
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class JokeInput(BaseModel):
    joke: str

@app.post("/api/analyze")
def analyze_joke(data: JokeInput):
    blob = TextBlob(data.joke)
    return {
        "polarity": round(blob.sentiment.polarity, 3),
        "subjectivity": round(blob.sentiment.subjectivity, 3)
    }