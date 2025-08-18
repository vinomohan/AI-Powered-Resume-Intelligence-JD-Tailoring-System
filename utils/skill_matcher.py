# utils/skill_matcher.py

def compare_skills(resume_skills, jd_skills):
    resume_skills_set = set([skill.lower() for skill in resume_skills])
    jd_skills_set = set([skill.lower() for skill in jd_skills])

    matched_skills = list(resume_skills_set & jd_skills_set)
    missing_skills = list(jd_skills_set - resume_skills_set)
    
    match_percentage = (len(matched_skills) / len(jd_skills_set) * 100) if jd_skills_set else 0.0

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }
