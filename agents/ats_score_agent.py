from bedrock_client import invoke_llm

def calculate_ats_score(skill_data):
    prompt = f"""
You are an ATS scoring engine.

INPUT:
Required skills: {skill_data["required_skills"]}
Matched skills: {skill_data["matched_skills"]}
Missing skills: {skill_data["missing_skills"]}

RULES:
- score 0–100
- critical skills weighted higher
- recruiter-like judgment
- NO explanation
- JSON only

FORMAT:
{{
  "ats_score": number,
  "summary": "short justification"
}}
"""
    return invoke_llm(prompt, temperature=0.2)
