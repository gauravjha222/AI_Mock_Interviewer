from openai import OpenAI

client = OpenAI(api_key=" ")

# modules/evaluator.py

def evaluate_answer(question, answer, use_mock=False):
    """
    Evaluate the answer to a question.
    If use_mock=True, return dummy feedback for demo purposes.
    """
    if use_mock:
        # Simple mock feedback
        return {
            "question": question,
            "answer": answer,
            "feedback": "Good attempt. Focus on clarity and examples.",
            "score": "8/10"
        }
    
    # Default offline behavior
    return {
        "question": question,
        "answer": answer,
        "feedback": "Evaluation not implemented (mock mode off).",
        "score": "N/A"
    }
