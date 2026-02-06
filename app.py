import streamlit as st
from openai import OpenAI

# ---------------- AI CLIENT ----------------
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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"
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📘",
    layout="centered"
)

# ---------------- STYLES ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
}
h1 {
    text-align: center;
    color: #00ffe7;
    text-shadow: 0 0 15px #00ffe7;
}
textarea {
    background-color: #111 !important;
    color: #00ffe7 !important;
    border-radius: 12px !important;
    border: 1px solid #00ffe7 !important;
}
button {
    background: linear-gradient(90deg, #00ffe7, #00ff88) !important;
    color: black !important;
    font-weight: bold !important;
    border-radius: 30px !important;
    padding: 10px 25px !important;
    box-shadow: 0 0 20px #00ffe7 !important;
}
button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px #00ff88 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ AI Study Buddy ⚡</h1>", unsafe_allow_html=True)

# ---------------- MEMORY ----------------
if "history" not in st.session_state:
    st.session_state.history = ""

# ---------------- INPUT ----------------
user_input = st.text_area(
    "Ask any topic or continue learning (MVJ Students)",
    placeholder="Example: What is deadlock? / Who are you? / Explain mutex"
)

# ---------------- BUTTON ----------------
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something first.")
    else:
        with st.spinner("Professor is explaining for MVJ students..."):

            full_prompt = f"""
You are a university professor named **A H Daniel Sharon**.

IDENTITY RULES (VERY IMPORTANT):
- Your name is A H Daniel Sharon
- You were created by A H Daniel Sharon
- You teach students of **MVJ College of Engineering**
- You must clearly say this if asked:
  • who are you
  • who created you
  • whom do you teach
  • what college students you help

TEACHING STYLE RULES:
- You are teaching **MVJ College of Engineering students**
- Frequently and naturally mention "MVJ College of Engineering" and "MVJ students"
- Be very friendly, supportive, and student-focused

TOPIC EXPLANATION RULES:
- If the student asks about a topic or concept:
  1. Give a VERY LONG, VERY CLEAR, beginner-friendly explanation
  2. Explain step by step, point by point
  3. Use headings, subheadings, and bullet points
  4. Give simple real-world examples relevant to engineering students
  5. Write as if preparing students for MVJ semester exams

AFTER EVERY TOPIC EXPLANATION (COMPULSORY):
- Give **ONLY**:
  --- 2 MARK QUESTIONS WITH ANSWERS ---
  (Minimum 5 questions, each with a clear answer)

  --- 10 MARK QUESTIONS WITH ANSWERS ---
  (Minimum 3 questions, each with a detailed answer)

CONVERSATION RULES:
- Remember previous discussion
- Continue naturally like a teacher talking to the same MVJ students
- Do not ask questions back unless clarification is truly needed

CONVERSATION HISTORY:
{st.session_state.history}

STUDENT MESSAGE:
{user_input}

Now respond appropriately.
"""

            response = client.responses.create(
                model="meta-llama/Meta-Llama-3-8B-Instruct",
                input=full_prompt
            )

            ai_reply = response.output_text

            st.session_state.history += f"\nStudent: {user_input}\nProfessor A H Daniel Sharon: {ai_reply}\n"

        st.subheader("📘 Professor A H Daniel Sharon (MVJ College of Engineering)")
        st.write(ai_reply)
