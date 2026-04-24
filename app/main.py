from fastapi import FastAPI
from app.routes import sentiment

app = FastAPI()

app.include_router(sentiment.router)

@app.get("/")
def root():
    return {"message": "API is running"}