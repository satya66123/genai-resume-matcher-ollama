import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.pipeline import run_pipeline

st.set_page_config(page_title="GenAI Resume Matcher", layout="wide")

st.title("🚀 GenAI Resume Matcher (Ollama Powered)")

st.write("Match your resume with job descriptions using AI/ML + GenAI")

# Input columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Resume")
    resume_text = st.text_area("Paste your resume here", height=300)

with col2:
    st.subheader("📋 Job Description")
    jd_text = st.text_area("Paste job description here", height=300)

# Button
if st.button("🔍 Analyze Match"):
    if resume_text and jd_text:
        with st.spinner("Analyzing..."):
            result = run_pipeline(resume_text, jd_text)

        st.success("Analysis Complete!")

        # Show Score
        st.subheader("📊 Match Score")
        st.metric(label="Similarity", value=f"{result['match_score']}%")

        # Show Feedback
        st.subheader("Feedback")
        st.write(result["ai_feedback"])

    else:
        st.warning("Please enter both Resume and Job Description")