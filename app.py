import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=""
)
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📘",
    layout="centered"
)

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


notes = st.text_area("Paste your study notes here")

if st.button("Summarize"):
    if notes.strip() == "":
        st.warning("Please paste some notes first.")
    else:
        with st.spinner("AI is thinking..."):
            response = client.responses.create(
                model="meta-llama/Meta-Llama-3-8B-Instruct",
                input = f"""
You are a top university professor and exam topper.

Explain the following topic in a VERY DETAILED way.

Rules:
- Use headings
- Use bullet points
- Explain clearly
- Give examples
- Make it suitable for exams
- Write a LONG answer

Topic:
{notes}
"""
            )

        st.subheader("AI Output")
        st.write(response.output_text)
