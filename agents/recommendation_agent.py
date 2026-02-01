from bedrock_client import invoke_llm

def generate_recommendations(skill_data):
    prompt = f"""
You are an ATS resume optimization engine.

TASK:
Generate resume improvement recommendations strictly based on missing skills.

INPUT:
Missing skills: {skill_data["missing_skills"]}

INSTRUCTIONS (STRICT):
- Focus ONLY on resume improvements
- Each recommendation must mention WHERE to update:
  (Skills section, Experience section, Projects section)
- Be specific and actionable
- Do NOT suggest learning resources
- Do NOT repeat the skill list verbatim
- Limit to MAX 5 recommendations
- Use professional ATS language
- JSON only

RECOMMENDATION TYPES:
- Skill inclusion
- Experience quantification
- Project showcasing
- Keyword alignment

FORMAT:
{{
  "recommendations": [
    "string",
    "string"
  ]
}}
"""
    return invoke_llm(prompt, temperature=0)
