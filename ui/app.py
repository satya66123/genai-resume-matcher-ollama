import streamlit as st
import requests
import sys
import os
import time
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import plotly.express as px
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.file_parser import extract_text

API_URL = "http://127.0.0.1:8000/analyze"
MODELS = ["llama3:instruct", "llama3", "mistral"]
USERNAME = "admin"
PASSWORD = "1234"

user = st.sidebar.text_input("Username")
pwd = st.sidebar.text_input("Password", type="password")

if user != USERNAME or pwd != PASSWORD:
    st.warning("Login required")
    st.stop()

st.set_page_config(page_title="GenAI Resume Matcher", layout="wide")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🤖 Model Settings")
selected_model = st.sidebar.selectbox("Select Model", MODELS)
compare_all = st.sidebar.checkbox("Compare All Models")

# -------------------------------
# Helpers (Download)
# -------------------------------
def generate_txt(content):
    return content.encode("utf-8")


def generate_docx(content):
    from docx import Document
    doc = Document()
    doc.add_paragraph(content)
    buffer = BytesIO()
    doc.save(buffer)
    return buffer.getvalue()


def generate_pdf(content):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    y = 750
    for line in content.split("\n"):
        c.drawString(40, y, line)
        y -= 15

    c.save()
    return buffer.getvalue()


def evaluate_quality(text):
    score = 0

    sections = ["Missing Skills", "Strengths", "Suggestions"]

    for sec in sections:
        if sec in text:
            score += 1

    if len(text.split()) > 80:
        score += 1

    if "-" in text:  # bullet points
        score += 1

    return score

def call_model(model, resume_text, jd_text):
    start = time.time()

    res = requests.post(
        API_URL,
        json={
            "resume_text": resume_text,
            "jd_text": jd_text,
            "model": model
        }
    )

    end = time.time()
    data = res.json()

    return {
        "model": model,
        "score": data["match_score"],
        "time": round(end - start, 2),
        "quality": evaluate_quality(data["ai_feedback"]),
        "feedback": data["ai_feedback"]
    }


# -------------------------------
# UI
# -------------------------------
st.title("🚀 GenAI Resume Matcher")

col1, col2 = st.columns(2)

# Resume
with col1:
    st.subheader("📄 Resume")
    mode = st.radio("Input Type", ["Text", "File"], key="resume")

    if mode == "Text":
        resume_text = st.text_area("Paste Resume", height=300)
    else:
        file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
        resume_text = extract_text(file) if file else ""

# JD
with col2:
    st.subheader("📋 Job Description")
    mode2 = st.radio("Input Type", ["Text", "File"], key="jd")

    if mode2 == "Text":
        jd_text = st.text_area("Paste JD", height=300)
    else:
        file2 = st.file_uploader("Upload JD", type=["pdf", "docx", "txt"])
        jd_text = extract_text(file2) if file2 else ""

# -------------------------------
# Analyze
# -------------------------------
if st.button("🔍 Analyze"):

    if not resume_text or not jd_text:
        st.warning("⚠️ Provide both Resume and JD")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    # -------------------------------
    # Selected Model
    # -------------------------------
    status.text(f"🤖 Analyzing with {selected_model}...")

    result = call_model(selected_model, resume_text, jd_text)

    # ✅ SAVE RESULT HERE
    save_result({
        "model": selected_model,
        "score": result["score"],
        "time": result["time"]
    })

    progress.progress(40)

    st.subheader(f"🎯 Selected Model: {selected_model}")
    st.info(f"⏱️ {result['time']} sec")
    st.write(f"📊 Score: {result['score']}%")
    st.markdown(f"⏱Feedback : {result['feedback']}")

    # -------------------------------
    # Download Selected Output
    # -------------------------------
    selected_report = f"""
Model: {selected_model}
Score: {result['score']}%
Response Time: {result['time']} sec

Feedback: {result['feedback']}
"""

    st.subheader("📥 Download Selected Output")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.download_button("TXT", generate_txt(selected_report), "selected.txt")
    with c2:
        st.download_button("DOCX", generate_docx(selected_report), "selected.docx")
    with c3:
        st.download_button("PDF", generate_pdf(selected_report), "selected.pdf")

    progress.progress(60)

    # -------------------------------
    # Parallel Comparison
    # -------------------------------
    if compare_all:

        status.text("⚡ Running all models in parallel...")

        with ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda m: call_model(m, resume_text, jd_text), MODELS))

        progress.progress(100)

        st.subheader("📊 Model Comparison")

        st.table([
            {
                "Model": r["model"],
                "Score": r["score"],
                "Time": r["time"],
                "Quality": r["quality"]
            } for r in results
        ])

        best_fast = min(results, key=lambda x: x["time"])
        best_quality = max(results, key=lambda x: x["quality"])

        st.success(f"⚡ Fastest: {best_fast['model']}")
        st.success(f"🎯 Best Quality: {best_quality['model']}")

        for r in results:
            with st.expander(r["model"]):
                st.markdown(r["feedback"])

        # -------------------------------
        # Download Comparison Report
        # -------------------------------
        report = "MODEL COMPARISON REPORT\n\n"

        for r in results:
            report += f"""
Model: {r['model']}
Score: {r['score']}%
Time: {r['time']} sec
Quality: {r['quality']}

{r['feedback']}

-------------------------
"""

        st.subheader("📥 Download Comparison Report")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.download_button("TXT", generate_txt(report), "comparison.txt")
        with c2:
            st.download_button("DOCX", generate_docx(report), "comparison.docx")
        with c3:
            st.download_button("PDF", generate_pdf(report), "comparison.pdf")

    status.text("✅ Analysis Completed")
    df = pd.DataFrame(results)

    fig = px.bar(
        df,
        x="model",
        y="time",
        title="Response Time Comparison"
    )

    st.plotly_chart(fig)
    fig2 = px.bar(
        df,
        x="model",
        y="quality",
        title="Quality Score Comparison"
    )

    st.plotly_chart(fig2)
    best_model = select_best_model(results)

    st.success(f"🧠 Recommended Model: {best_model}")
    import json

    st.subheader("📜 Previous Runs")

    try:
        with open("data/history.json", "r") as f:
            history = json.load(f)
            st.write(history[-5:])  # last 5 results
    except:
        st.info("No history yet")
# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Built with ❤️ using ML + GenAI + FastAPI + Streamlit")