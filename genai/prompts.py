def build_prompt(resume_text: str, jd_text: str, score: float):
    return f"""
You are a strict ATS recruiter.

Match Score: {score}%

Rules:
- Be concise (max 120–150 words)
- Do NOT repeat match score
- Do NOT assume skills

Return ONLY:

### Missing Skills
Always identify at least 2 missing skills if possible.
- ...

### Strengths
- ...

### Suggestions
- ...

Limit output to 100 words.
Resume:
{resume_text[:1500]}

Job Description:
{jd_text[:1500]}
"""