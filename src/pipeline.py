from src.preprocess import preprocess_documents
from src.similarity import compute_similarity
from genai.prompts import build_prompt
from genai.ollama_client import generate_response


def run_pipeline(resume_text: str, jd_text: str, model: str = "llama3:instruct"):
    resume_clean, jd_clean = preprocess_documents(resume_text, jd_text)

    score = compute_similarity(resume_clean, jd_clean)

    prompt = build_prompt(resume_text, jd_text, score)
    ai_feedback = generate_response(prompt, model=model)

    return {
        "match_score": score,
        "ai_feedback": ai_feedback
    }
def select_best_model(results):
    best = sorted(
        results,
        key=lambda x: (x["quality"], -x["time"]),
        reverse=True
    )[0]

    return best["model"]