import re
from nltk.tokenize import word_tokenize
from utils.common_skills import COMMON_SKILLS

def extract_keywords_from_jd(jd_text):
    # Normalize JD text
    jd_text = jd_text.lower()
    jd_text = jd_text.replace("/", " ").replace("-", " ")  # Handle PHP/Laravel-style tokens
    jd_text = re.sub(r'[^a-z0-9\s]', ' ', jd_text)  # Remove punctuation

    # Tokenize and create n-grams (up to 3-word phrases)
    words = word_tokenize(jd_text)
    tokens = set(words)

    # Also include 2-gram and 3-gram phrases
    bigrams = {' '.join(words[i:i+2]) for i in range(len(words)-1)}
    trigrams = {' '.join(words[i:i+3]) for i in range(len(words)-2)}

    jd_keywords = tokens.union(bigrams).union(trigrams)

    # Match with known skill set
    matched_skills = sorted({skill for skill in COMMON_SKILLS if skill in jd_keywords})

    return matched_skills
