# 🧠 AI-Powered Resume Intelligence & JD Tailoring System

A hands-on **GenAI student project** that leverages **NLP, local LLMs (Mistral 7B)**, and a **Flask-based web interface** to provide meaningful, secure, and offline-capable resume insights. Designed to simulate how a smart recruiter would evaluate resumes against job descriptions.

---

## 🚀 Features

- 📄 **Resume Parser** from PDF/DOCX with email, phone, and skill extraction
- 🔍 **Job Description Parser** using SpaCy + Regex for key skill identification
- 🎯 **Skill Matching Engine** to compute match percentage & identify missing skills
- 🧠 **LLM-Powered Suggestions** using locally hosted **Mistral 7B GGUF model**
- 🧾 **Tailored Resume Text** output with skill enrichment and refinement
- ✉️ **Cover Letter Generator** using LLMs trained on tone and context
- ⬇️ Downloadable cover letter option (TXT format)
- 🔒 Fully **offline and privacy-safe** architecture

---

## 🧰 Tech Stack

| Area                  | Tool / Framework                   |
|-----------------------|------------------------------------|
| Backend Logic         | Python                             |
| Web App               | Flask + Jinja2                     |
| NLP                   | SpaCy + Regex                      |
| Resume Parsing        | PyMuPDF (PDF), python-docx (DOCX)  |
| LLM Integration       | Mistral 7B (gguf via llama-cpp)    |
| AI Feedback Module    | Prompt engineering with context    |
| File Handling         | werkzeug + os                      |
| Deployment            | Localhost Flask app                |

---

## 📊 How It Works

1. **Upload Resume (PDF/DOCX)** + Paste **Job Description**
2. Backend extracts:
   - Email, Phone, Skills from Resume
   - Skills from Job Description
3. A **Skill Matching Engine** compares and calculates:
   - ✅ Matched Skills
   - ❌ Missing Skills
   - 📈 Match Percentage
4. A **local LLM (Mistral 7B)** generates:
   - ✍️ Suggestions to improve resume
   - 📝 Tailored Resume Content
   - 💌 AI-generated Cover Letter
5. Cover letter can be **downloaded as .txt**
6. Results displayed in a modern, professional UI

---

## 📁 Project Structure

```plaintext
resume_ai_app/
│
├── app.py                         # Flask backend
├── templates/
│   ├── index.html                 # Upload page
│   └── results.html              # Results + download
├── static/
│   └── styles.css                # Custom styles
├── models/
│   └── mistral-model.gguf        # Local LLM file
├── utils/
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── skill_matcher.py
│   └── llm_feedback.py
└── README.md
