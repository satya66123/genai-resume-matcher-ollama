from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="GenAI Resume Matcher API")

app.include_router(router)