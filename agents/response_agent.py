def build_response(skill_data, score_data, rec_data, decision_data):
    return {
        "match_percentage": score_data["ats_score"],
        "matched_skills": skill_data["matched_skills"],
        "missing_skills": skill_data["missing_skills"],
        "recommendations": rec_data["recommendations"],
        "should_apply": decision_data["decision"],
        "decision_reason": decision_data["reason"]
    }
