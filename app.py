import streamlit as st
import random
import time

from modules.resume_parser import extract_text_from_pdf, extract_keywords, extract_projects
from modules.question_generator import generate_interview_questions
from modules.stt_module import speech_to_text
from modules.evaluator import evaluate_answer

st.set_page_config(page_title="AI Mock Interview Bot", layout="wide")
st.title("🎤 AI Mock Interview Bot")

# ---------------- SESSION STATES ----------------
if "questions" not in st.session_state:
    st.session_state.questions = []
if "answers" not in st.session_state:
    st.session_state.answers = []
if "evaluations" not in st.session_state:
    st.session_state.evaluations = []
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# ----------- STEP 1: UPLOAD RESUME ---------------
st.header("📄 Step 1: Upload Resume")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded!")

    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Resume Text")
    st.text_area("", text, height=200)

    keywords = extract_keywords(text)
    projects = extract_projects(text)

    st.write("### 🔍 Extracted Skills:", keywords)
    st.write("### 📌 Extracted Projects:", projects)

    if st.button("Generate Interview Questions"):
        all_questions = generate_interview_questions(keywords, projects)
        st.session_state.questions = all_questions
        st.session_state.question_index = 0
        st.session_state.answers = []
        st.session_state.evaluations = []

        st.success("Questions Generated! Move to Step 2.")

# ----------- STEP 2: INTERVIEW MODE ---------------
st.header("🎧 Step 2: Interview Session")

if len(st.session_state.questions) > 0:
    idx = st.session_state.question_index
    total = len(st.session_state.questions)

    if idx < total:
        question = st.session_state.questions[idx]
        st.markdown(f"### **Question {idx+1}/{total}:** {question}")

        # ⏳ 3-minute timer
        with st.expander("Timer (3 minutes)"):
            for remaining in range(180, 0, -1):
                st.write(f"⏳ Time left: {remaining} seconds")
                time.sleep(1)

        # Answer: Audio / Text
        audio_bytes = st.audio_input("🎙️ Speak your answer")
        text_answer = ""

        if audio_bytes:
            st.audio(audio_bytes)
            st.info("Converting audio to text...")
            text_answer = speech_to_text(audio_bytes)
            st.success("Your speech converted to text.")
            st.write(text_answer)
        else:
            text_answer = st.text_area("Or type your answer:")

        if st.button("Save & Next Question"):
            if text_answer.strip() == "":
                st.warning("Please answer before proceeding.")
            else:
                st.session_state.answers.append(text_answer)

                # Evaluate automatically
                eval_result = evaluate_answer(question, text_answer)
                st.session_state.evaluations.append(eval_result)

                st.session_state.question_index += 1
                st.experimental_rerun()

# ----------- STEP 3: SUMMARY ---------------
if len(st.session_state.answers) == len(st.session_state.questions) and len(st.session_state.answers) > 0:
    st.header("📊 Final Interview Evaluation Report")

    for i, item in enumerate(st.session_state.evaluations):
        st.subheader(f"Question {i+1}")
        st.write(f"**Q:** {item['question']}")
        st.write(f"**Your answer:** {item['answer']}")
        st.write(f"**Score:** {item['score']}")
        st.write(f"**Feedback:** {item['feedback']}")
        st.write(f"**Strengths:** {item['strengths']}")
        st.write(f"**Improvements:** {item['improvements']}")
        st.markdown("---")
