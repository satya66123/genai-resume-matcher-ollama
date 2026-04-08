from src.pipeline import run_pipeline

resume = """
Python developer with strong experience in machine learning, NLP,
deep learning, FastAPI, REST APIs, and model deployment, building AI-driven applications, performing data preprocessing,
feature engineering, model training, and deploying ML models in scalable backend systems.
"""

jd = """
We are hiring a Python developer with strong experience in machine learning, NLP,
deep learning, FastAPI, REST APIs, and model deployment.

Candidate should have experience building AI-driven applications, performing data preprocessing,
feature engineering, model training, and deploying ML models in scalable backend systems.
"""
result = run_pipeline(resume, jd)
print(result)