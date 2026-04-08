import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def preprocess_documents(resume_text: str, jd_text: str):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)
    return resume_clean, jd_clean