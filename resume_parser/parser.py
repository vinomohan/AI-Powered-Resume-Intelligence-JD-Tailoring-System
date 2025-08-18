import os
import re
import docx2txt
from pdfminer.high_level import extract_text

# Load common skill set
from utils.common_skills import COMMON_SKILLS

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text(file_path)
    elif ext == '.docx':
        return docx2txt.process(file_path)
    else:
        return ""

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-()]{7,}\d', text)
    return match.group(0) if match else None

def extract_skills(text):
    text_lower = text.lower()
    return list({skill for skill in COMMON_SKILLS if skill in text_lower})

def parse_resume(file_path):
    try:
        full_text = extract_text_from_file(file_path)
        if not full_text.strip():
            return {"error": "Could not extract text from file"}

        data = {
            "email": extract_email(full_text),
            "phone": extract_phone(full_text),
            "skills": extract_skills(full_text),
            "raw_text": full_text[:1500] + "..."  # limit for preview
        }
        return data

    except Exception as e:
        return {"error": str(e)}
