from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf

from agents.input_agent import process_input
from agents.skill_match_agent import extract_and_match_skills
from agents.ats_score_agent import calculate_ats_score
from agents.recommendation_agent import generate_recommendations
from agents.decision_agent import make_apply_decision
from agents.response_agent import build_response
from agents.error_agent import handle_error

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    analysis = None

    if request.method == "POST":
        try:
            resume = request.files["resume"]
            job_desc = request.form["job_desc"]

            resume_text = extract_text_from_pdf(resume)

            data = process_input(resume_text, job_desc)

            skill_data = extract_and_match_skills(
                data["resume_text"], data["job_desc"]
            )

            score_data = calculate_ats_score(skill_data)
            rec_data = generate_recommendations(skill_data)
            decision_data = make_apply_decision(
                score_data["ats_score"], skill_data
            )

            analysis = build_response(
                skill_data, score_data, rec_data, decision_data
            )

        except Exception as e:
            analysis = handle_error(e)

    return render_template("index.html", analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)
