from src.pipeline import run_pipeline

resume = """
Python developer with experience in machine learning, NLP, deep learning,
FastAPI, REST APIs, data preprocessing, model training, and deployment.
Worked on AI-driven solutions and backend systems.
"""

jd = """
We are hiring a Python developer with strong experience in machine learning,
NLP, deep learning, FastAPI, REST API development, and model deployment.
"""

result = run_pipeline(resume, jd)
print(result)