from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

analyzer = SentimentIntensityAnalyzer()

# Request schema
class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "API is running"}

# sentiment analysis endpoint
@app.post("/analyze/sentiment")
def analyze_sentiment(request: TextRequest):
    text = request.text

    if not text or not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "positive"
    elif compound <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "sentiment": sentiment,
        "score": compound,
        "details": scores
    }