from genai.ollama_client import generate_response
from genai.prompts import build_prompt
from src.preprocess import preprocess_documents
from src.similarity import compute_similarity


def run_pipeline(resume_text: str, jd_text: str):
    resume_clean, jd_clean = preprocess_documents(resume_text, jd_text)

    score = compute_similarity(resume_clean, jd_clean)

    prompt = build_prompt(resume_text, jd_text, score)
    ai_feedback = generate_response(prompt)

    return {
        "match_score": score,
        "ai_feedback": ai_feedback
    }