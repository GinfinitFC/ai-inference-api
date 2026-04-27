from fastapi import APIRouter, HTTPException
from app.models.schemas import BatchRequest
from app.services.sentiment_service import analyze_sentiment_logic

router = APIRouter()

@router.post("/analyze/batch")
def analyze_batch(request: BatchRequest):
    texts = request.texts

    if not texts or len(texts) == 0:
        raise HTTPException(status_code=400, detail="Text list cannot be empty")

    if len(texts) > 10:
        raise HTTPException(status_code=400, detail="Too many texts (max 10)")

    results = []

    for text in texts:
        if not text.strip():
            results.append({"error": "Empty text"})
        else:
            result = analyze_sentiment_logic(text)
            results.append({'Input':text, 'Output': result})

    return {
        "status": "success",
        "results": results
    }