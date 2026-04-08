from src.preprocess import preprocess_documents
from src.similarity import compute_similarity


def run_pipeline(resume_text: str, jd_text: str):
    resume_clean, jd_clean = preprocess_documents(resume_text, jd_text)

    score = compute_similarity(resume_clean, jd_clean)

    return {
        "match_score": score
    }