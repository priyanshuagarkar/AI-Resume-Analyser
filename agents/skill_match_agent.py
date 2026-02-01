from bedrock_client import invoke_llm

def extract_and_match_skills(resume_text, job_desc):
    prompt = f"""
You are an ATS NLP engine.

TASK:
- Extract required job skills
- Match resume skills semantically
- Identify missing skills

RULES:
- lowercase
- semantic matches allowed
- NO explanation
- JSON only

FORMAT:
{{
  "required_skills": [string],
  "matched_skills": [string],
  "missing_skills": [string]
}}

Resume:
{resume_text}

Job Description:
{job_desc}
"""
    return invoke_llm(prompt, temperature=0.2)
