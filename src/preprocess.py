import re


def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def preprocess_documents(resume_text: str, jd_text: str):
    return clean_text(resume_text), clean_text(jd_text)