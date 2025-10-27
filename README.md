<h1>  # AI_Mock_Interviewer </h1>

This project is an AI Voice Mock Interviewer app built with Streamlit. Here’s a detailed explanation suitable for presentation, covering its goals, workflow, technical architecture, and highlights.

<h3> * Project Goal </h3>>

1. Simulate a real technical interview for AI/ML/Data Science roles.
2. Automatically generate skill-based interview questions from the candidate’s own resume.

3. Allow candidates to respond verbally, recording answers for later review and self-assessment.

   

<h3> 💻 How It Works: End-to-End Interview Pipeline </h3>

1. User Interface
   
The app is web-based, built using Streamlit for interactive UI.

Candidate uploads their resume (PDF format) using a simple drag-and-drop widget.

2. Resume Parsing & Skill Extraction
   
On upload, the app parses the PDF, reads the textual content, and scans for important keywords linked to AI/ML/DS topics (e.g., "machine learning", "deep learning", "Python", "statistics", "NLP", etc.).

The resume parser uses simple keyword matching for speed and reliability, and lists the detected skills on the screen for transparency.

3. Tailored Question Generation
   
A pre-defined question bank is organized by topic (ML, DL, Stats, Data Science, etc.).

The app randomly selects questions from relevant topics—if your resume contains ML and DL, it will ask from both, not just one.

Each interview session generates a new, balanced set of challenging questions.

4. Interactive Interview Workflow
   
Questions are shown one by one, with proper numbering (e.g. "Question 1/10").

For every question, a timer starts (default 2 minutes, can be ended early).

The candidate can answer verbally; their response is recorded.

5. Voice Recording and Submission
   
Each answer is saved as an audio file (response_qN.wav) for future review.

Candidates control the pace: they can press "Submit Answer / Next Question" anytime if they finish early, or wait for the timer to end.

6. Completion and Storage
   
After all questions, the interface displays a “Interview completed!” message and resets.

All recorded answers remain stored locally for the user to play back or evaluate.



<h3> 🛠️ Technical Architecture </h3>


Streamlit: Rapid prototyping and interactive UI.

resume_parser.py: PDF reading and keyword-based skill extraction (using PyPDF2).

question_generator.py: Topic-balanced random question selection.

audio_recorder_streamlit: For easy microphone integration and answer recording.

Sessions/State Management: Uses Streamlit’s session_state to keep track of progress, timer, and answers.

<h3> ✨ Features and Highlights </h3>

Intelligent mock interview tailored to the candidate’s own background, not generic.

Speech-based practice: Candidates answer naturally, like a real interview.

Session progress: Clean question flow, live timer, and one-click advance or submission.

Answer review: Audio saved per question for self-assessment or sharing.

Extensible: Easy to add NLP-based transcription, scoring, or analytics for further improvement.

<h3> 🔎 What Makes It Stand Out </h3>

Mimics the real-world interview scenario—time-limited, voice-based, and skill-adaptive.

Useful as a resume project for Data Science, AI/ML, or software roles.

Demonstrates integration of Python file handling, keyword NLP, and interactive web-app design.

<h3> 👨‍💻 Typical User Experience </h3>

Upload resume → see skills detected.

Receive personalized technical questions in a random order.

Record voice answers and submit before or after timer.

Repeat for 10 questions, then review saved answers locally.
