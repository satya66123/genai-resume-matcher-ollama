from fastapi import APIRouter
from app.schemas import AnalyzeRequest, AnalyzeResponse
from src.pipeline import run_pipeline

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(data: AnalyzeRequest):
    result = run_pipeline(
        data.resume_text,
        data.jd_text,
        data.model
    )
    return result