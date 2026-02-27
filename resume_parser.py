# modules/resume_parser.py

import PyPDF2
import re

# Expanded list of technical skills for CSE / AI / ML / Data Science
TECH_SKILLS = [
    "python", "java", "c++", "c", "sql", "nosql", "mongodb", "postgresql",
    "ml", "ai", "deep learning", "nlp", "computer vision", "data science",
    "pytorch", "tensorflow", "keras", "scikit-learn", "opencv", "matplotlib",
    "seaborn", "pandas", "numpy", "flask", "django", "react", "angular",
    "docker", "kubernetes", "rest api", "graphql", "aws", "azure", "gcp",
    "linux", "git", "gitlab", "github", "bash", "shell scripting", "regex",
    "lstm", "rnn", "transformers", "cnn", "ann", "svm", "decision trees",
    "random forest", "xgboost", "data visualization", "tableau", "power bi",
    "spark", "hadoop", "etl", "big data", "reinforcement learning", "robotics"
]

def extract_text_from_pdf(pdf_file):
    """
    Extract all text from a PDF file.
    """
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def extract_keywords(text):
    """
    Extract technical keywords from the resume text.
    """
    found = set()
    text_lower = text.lower()

    for skill in TECH_SKILLS:
        # Match whole words or phrases
        if re.search(rf'\b{re.escape(skill.lower())}\b', text_lower):
            found.add(skill)

    return list(found)

def extract_projects(text):
    """
    Extract project-related lines from resume.
    Looks for lines containing 'project' or typical project keywords.
    """
    lines = text.split("\n")
    projects = []

    project_keywords = ["project", "internship", "capstone", "research", "work done"]
    for line in lines:
        for kw in project_keywords:
            if kw in line.lower() and len(line.strip()) > 10:
                projects.append(line.strip())
                break  # avoid duplicates if multiple keywords match

    return projects
