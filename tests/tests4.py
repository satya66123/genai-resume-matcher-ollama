from src.pipeline import run_pipeline

resume = """
Python developer with strong experience in machine learning, NLP, deep learning,
FastAPI, REST APIs, model training, evaluation, and deployment.
Worked on AI-driven applications, data preprocessing, and scalable backend systems.
"""

jd = """
We are hiring a Python developer with expertise in machine learning, NLP,
deep learning, FastAPI, REST API development, and model deployment.
Experience with scalable backend systems and AI-driven applications is required.
"""

result = run_pipeline(resume, jd)
print(result)