from fastapi import APIRouter, HTTPException
from app.models.schemas import TextRequest
from app.services.sentiment_service import analyze_sentiment_logic

router = APIRouter()

@router.post("/analyze/sentiment")
def analyze_sentiment(request: TextRequest):
    text = request.text

    if not text or not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    return {"status":"success", "data":analyze_sentiment_logic(text)}