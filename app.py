import os
from flask import Flask, render_template, request
from flask import send_file
import io



# Import utilities
from resume_parser.parser import parse_resume
from jd_parser.jd_extractor import extract_keywords_from_jd
from utils.skill_matcher import compare_skills
from generators.resume_tailor import generate_tailored_resume
from generators.cover_letter_gen import generate_cover_letter

app = Flask(__name__)


@app.route('/download_cover_letter', methods=['POST'])
def download_cover_letter():
    cover_letter_text = request.form.get('cover_letter_text')
    if not cover_letter_text:
        return "❌ No cover letter to download.", 400

    buffer = io.BytesIO()
    buffer.write(cover_letter_text.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer,
                     as_attachment=True,
                     download_name="Cover_Letter.txt",
                     mimetype='text/plain')

# Directory to store uploaded resumes
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Resume & JD from form
        resume_file = request.files.get('resume')
        job_description = request.form.get('job_description')

        if not resume_file or resume_file.filename == '':
            return "❌ No resume file uploaded.", 400
        if not job_description:
            return "❌ Job description is required.", 400

        # Save uploaded resume
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(resume_path)

        # Step 1: Parse resume
        parsed_resume = parse_resume(resume_path)

        # Step 2: Extract JD skills
        jd_skills = extract_keywords_from_jd(job_description)

        # Step 3: Skill match report
        skill_comparison = compare_skills(parsed_resume.get("skills", []), jd_skills)

        # Step 4: Suggestions from LLM
        from llm_utils.local_llm import get_llm_response
        suggestion_prompt = f"""
You are an expert career coach. Based on the following job description and candidate resume text, give 5 resume improvement suggestions:

Resume:
{parsed_resume.get('raw_text', '')}

Job Description:
{job_description}
"""
        suggestions = get_llm_response(suggestion_prompt)

        # Step 5: Tailor resume
        tailored_resume = generate_tailored_resume(parsed_resume.get("raw_text", ""), job_description)

        # Step 6: Generate cover letter
        cover_letter = generate_cover_letter(parsed_resume.get("raw_text", ""), job_description)

        return render_template(
            'results.html',
            parsed_resume=parsed_resume,
            jd_skills=jd_skills,
            skill_comparison=skill_comparison,
            suggestions=suggestions,
            tailored_resume=tailored_resume,
            cover_letter=cover_letter
        )

    # GET method
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
