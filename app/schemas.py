from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    resume_text: str
    jd_text: str


class AnalyzeResponse(BaseModel):
    match_score: float
    ai_feedback: str