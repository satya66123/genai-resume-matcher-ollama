from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(resume_text: str, jd_text: str) -> float:
    documents = [resume_text, jd_text]

    vectorizer = TfidfVectorizer()  # ❗ no stop_words for now
    tfidf_matrix = vectorizer.fit_transform(documents)

    if tfidf_matrix.shape[1] == 0:
        return 0.0

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(score[0][0]) * 100, 2)