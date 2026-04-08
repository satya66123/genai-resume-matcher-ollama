import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="GenAI Resume Matcher API")

app.include_router(router)