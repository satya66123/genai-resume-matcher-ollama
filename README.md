# 🚀 GenAI Resume Matcher (Multi-Model AI System)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Scikit-Learn](https://img.shields.io/badge/ML-ScikitLearn-orange)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![ATS Friendly](https://img.shields.io/badge/ATS-Optimized-success)
![SEO Ready](https://img.shields.io/badge/SEO-Optimized-blueviolet)

---

## 🧠 Overview

**GenAI Resume Matcher** is a production-ready AI system that intelligently matches resumes with job descriptions using a hybrid approach of **Machine Learning + Generative AI**.

It leverages **TF-IDF + Cosine Similarity** for precise matching and enhances insights with **LLMs (via Ollama)** to generate human-like feedback, making it a powerful tool for job seekers and recruiters.

---

## 🔥 Key Features

* 📄 **Resume ↔ Job Description Matching**
* 📊 **TF-IDF + Cosine Similarity Scoring**
* 🤖 **AI-Powered Feedback (Local LLMs)**
* 🔄 **Multi-Model Comparison**

  * llama3
  * llama3:instruct
  * mistral
* ⚡ **Parallel Model Execution**
* ⏱️ **Response Time Tracking**
* 📊 **Benchmarking (Speed vs Quality)**
* 📁 **Multi-format File Upload (PDF, DOCX, TXT)**
* 📥 **Downloadable Reports (PDF, DOCX, TXT)**
* 🎯 **Clean UI with Streamlit + FastAPI Backend**

---

## 🏗️ System Architecture

```
Streamlit UI
     ↓
FastAPI Backend
     ↓
ML Engine (TF-IDF + Cosine Similarity)
     ↓
GenAI Layer (Ollama LLMs)
```

---

## 🧰 Tech Stack

| Layer        | Technology Used     |
| ------------ | ------------------- |
| Language     | Python              |
| Backend      | FastAPI             |
| Frontend     | Streamlit           |
| ML           | Scikit-learn        |
| GenAI        | Ollama (LLMs)       |
| File Parsing | PyPDF2, python-docx |
| Reports      | ReportLab           |

---

## ▶️ Run Locally

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Setup LLM Models (Ollama)

```bash
ollama pull llama3
ollama pull llama3:instruct
ollama pull mistral
```

### 3️⃣ Start Backend

```bash
uvicorn app.main:app --reload
```

### 4️⃣ Launch UI

```bash
streamlit run ui/app.py
```

---

## 📊 Example Output

* ✅ Match Score: **88.43%**
* 📉 Missing Skills
* 💪 Strengths
* 🧠 AI Suggestions
* ⏱️ Response Time
* 📊 Model Comparison Dashboard

---

## 📈 Model Benchmarking

| Model           | Speed ⚡ | Quality 🧠 |
| --------------- | ------- | ---------- |
| llama3          | Medium  | High       |
| llama3:instruct | Fast    | Medium     |
| mistral         | Fastest | Balanced   |

---

## 💡 Key Learnings

* ⚖️ Trade-offs between **accuracy vs speed**
* 🧠 Effective **prompt engineering** for structured outputs
* ⚡ **Parallel execution** improves performance significantly
* 🏗️ Designing **real-world scalable AI systems**

---

## 🚀 Future Updates

* 🔍 Semantic search using embeddings (FAISS / Vector DB)
* 🌐 Deploy on cloud (AWS / GCP / Azure)
* 🧑‍💼 Recruiter dashboard with analytics
* 📊 Advanced skill gap visualization
* 🔐 User authentication & profile management
* 📱 Mobile-responsive UI improvements
* 🤖 Integration with GPT APIs for comparison
* 📎 LinkedIn resume import feature

---

## 🏆 Highlights

* 🧠 Multi-model AI benchmarking system
* ⚡ High-performance parallel execution
* 🏗️ Production-level full-stack architecture
* 📊 Insightful AI-generated feedback system

---

## 📌 SEO Keywords

AI Resume Matcher, Resume Screening AI, Job Matching System, GenAI Projects, FastAPI AI App, Streamlit AI App, LLM Resume Analyzer, Machine Learning Resume Matching

---

## 👨‍💻 Author

** Satya Srinath Nekkanti **
Built with ❤️ using Machine Learning & Generative AI

---

## 🎉 Project Completion Badge

![Project Completed](https://img.shields.io/badge/Status-Project%20Completed-success?style=for-the-badge)

---
