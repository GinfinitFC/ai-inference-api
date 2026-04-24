from fastapi import APIRouter, HTTPException
from app.models.schemas import TextRequest
from app.services.summarize_service import summarize_text

router = APIRouter()

@router.post("/analyze/summarize")
def summarize(request: TextRequest):
    text = request.text

    if not text or not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    return summarize_text(text)