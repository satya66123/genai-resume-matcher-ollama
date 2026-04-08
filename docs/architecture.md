# 🏗️ System Architecture

## Overview

The application follows a modular full-stack AI architecture:


Frontend (Streamlit)

↓

Backend API (FastAPI)

↓

ML Layer (TF-IDF + Cosine Similarity)

↓

GenAI Layer (Ollama LLMs)


---

## Components

### 1. UI Layer (Streamlit)
- User input (text/file)
- Model selection
- Output display
- Report download

### 2. API Layer (FastAPI)
- Endpoint: `/analyze`
- Handles request/response
- Connects UI with pipeline

### 3. ML Layer
- Preprocessing
- TF-IDF vectorization
- Cosine similarity scoring

### 4. GenAI Layer
- Prompt engineering
- LLM inference (Ollama)
- Structured feedback generation

---

## Data Flow

1. User inputs resume + JD
2. UI sends request to API
3. API calls pipeline
4. Pipeline:
   - preprocesses text
   - computes similarity
   - generates AI feedback
5. Response returned to UI
