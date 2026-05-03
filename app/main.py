from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1 import api_router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Learning Platform"}
