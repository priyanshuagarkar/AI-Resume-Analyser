from bedrock_client import invoke_llm

def make_apply_decision(score, skill_data):
    prompt = f"""
You are an ATS decision engine.

Your job has TWO parts:
1. Apply the decision rules EXACTLY as written
2. Explain the decision in recruiter-friendly language

DO NOT invent new rules.
DO NOT restate numeric thresholds in the explanation.

INPUT:
ATS Score: {score}
Missing skills: {skill_data["missing_skills"]}

DECISION RULES (STRICT):
- If ATS Score >= 75 AND Missing skills count <= 2 → decision = "Yes"
- If ATS Score >= 60 → decision = "Maybe"
- Else → decision = "No"

REASON GUIDELINES:
- Explain the decision in plain English
- Mention skill gaps if relevant
- Mention readiness level (strong / partial / weak)
- Do NOT mention numeric thresholds (like 60 or 75)
- Keep it concise and professional

OUTPUT RULES:
- Always follow the decision rules
- The same input must always produce the same output
- JSON only

FORMAT:
{{
  "decision": "Yes | Maybe | No",
  "reason": "human-readable explanation"
}}
"""
    return invoke_llm(prompt, temperature=0)
