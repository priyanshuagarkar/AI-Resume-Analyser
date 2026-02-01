def process_input(resume_text, job_desc):
    if not resume_text or not job_desc:
        raise ValueError("Resume or Job Description missing")

    return {
        "resume_text": resume_text,
        "job_desc": job_desc
    }
