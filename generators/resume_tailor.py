from llm_utils.local_llm import get_llm_response

def generate_tailored_resume(resume_text, job_description):
    prompt = f"""
You are a resume expert. Given the resume and job description below, rewrite the resume to better align with the job while maintaining truthfulness.

### Resume:
{resume_text}

### Job Description:
{job_description}

### Tailored Resume:
"""
    return get_llm_response(prompt).strip()
