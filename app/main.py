from fastapi import FastAPI
from app.routes import sentiment, summarize, batch, health

app = FastAPI()

app.include_router(health.router)
app.include_router(sentiment.router)
app.include_router(summarize.router)
app.include_router(batch.router)

@app.get("/")
def root():
    return {"message": "API is running"}