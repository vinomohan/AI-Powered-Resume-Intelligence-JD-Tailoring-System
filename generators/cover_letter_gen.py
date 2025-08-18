from llm_utils.local_llm import get_llm_response

def generate_cover_letter(resume_text, job_description):
    prompt = f"""
You are a professional cover letter writer. Based on the following resume and job description, generate a concise and personalized cover letter. Make sure it includes:
- An introduction
- How the candidate matches the role
- A polite closing

### Resume:
{resume_text}

### Job Description:
{job_description}

### Cover Letter:
"""
    return get_llm_response(prompt).strip()
