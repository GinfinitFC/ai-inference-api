from fastapi import FastAPI
from app.routes import sentiment, summarize

app = FastAPI()

app.include_router(sentiment.router)
app.include_router(summarize.router)

@app.get("/")
def root():
    return {"message": "API is running"}