from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    resume_text: str
    jd_text: str
    model: str = "llama3:instruct"


class AnalyzeResponse(BaseModel):
    match_score: float
    ai_feedback: str