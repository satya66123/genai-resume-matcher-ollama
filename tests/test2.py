from src.pipeline import run_pipeline

resume = """
Python developer with experience in machine learning, deep learning,
NLP, FastAPI, data analysis, model training, and API development.
"""

jd = """
Looking for a Python developer skilled in machine learning,
NLP, deep learning, FastAPI, and building backend APIs.
"""

result = run_pipeline(resume, jd)
print(result)