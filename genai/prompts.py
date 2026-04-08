def build_prompt(resume_text: str, jd_text: str, score: float):
    return f"""
You are an AI career assistant.

Match Score: {score}%

Analyze the resume and job description.

Give:
1. Missing skills
2. Strengths
3. Improvement suggestions

Resume:
{resume_text}

Job Description:
{jd_text}
"""