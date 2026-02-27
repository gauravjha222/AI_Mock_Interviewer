
import random
from openai import OpenAI

client = OpenAI(api_key=" ")


# Default project-based questions
DEFAULT_PROJECT_QUESTIONS = [
    "Describe a challenge you faced in your last project and how you solved it.",
    "What technologies did you use in your project and why?",
    "How did you ensure the project was completed on time and with quality?",
    "Explain one technical decision you made in your project and its impact.",
    "How did you handle collaboration or conflicts in your project?"
]

def generate_interview_questions(keywords, projects, use_mock=False):
    """
    Generate 10 interview questions:
    - 7 AI-generated random questions from keywords
    - 3 project-based questions from default pool
    """
    if use_mock:
        # Just return fixed demo questions
        return [
            "Can you explain your experience with Python?",
            "What is your approach to solving data science problems?",
            "Tell me about a machine learning project you worked on.",
            "How do you handle missing data in a dataset?",
            "Explain a deep learning model you have implemented.",
            "What are your favorite libraries for NLP tasks?",
            "How do you optimize a model for better performance?",
            "Tell me about a challenge you faced in a project and how you solved it.",
            "How do you stay updated with the latest AI/ML research?",
            "Explain your understanding of LLMs and transformers."
        ]

    # ----------------- AI-Generated Questions -----------------
    if not keywords:
        keywords = ["python", "ml", "ai", "data science"]  # fallback

    # Prepare prompt for OpenAI
    prompt = f"""
    Act as an interview question generator.
    Using the following skills/keywords: {keywords}
    Generate 7 unique, varied, and random interview questions for a candidate.
    Only provide the questions as a numbered list.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        ai_questions = response.choices[0].message.content.split("\n")
        ai_questions = [q.strip() for q in ai_questions if q.strip()]
    except Exception as e:
        # fallback if OpenAI fails
        ai_questions = [
            f"What can you do with {kw}?" for kw in keywords[:7]
        ]

    ai_questions = ai_questions[:7]  # take first 7

    # ----------------- Project-Based Questions -----------------
    proj_questions = random.sample(DEFAULT_PROJECT_QUESTIONS, 3)

    # Combine and shuffle questions
    all_questions = ai_questions + proj_questions
    random.shuffle(all_questions)

    return all_questions
