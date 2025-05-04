import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Page setup
st.set_page_config(page_title="Start-Up Idea Generator", page_icon=":bulb:")

st.title("Start Your Startup Journey!")
st.subheader("Input your ideas and generate a complete startup plan.")

# Input method selection
input_mode = st.radio("Choose your input method:", ("Keywords", "Problem Statement"))

if input_mode == "Keywords":
    keywords = st.multiselect(
        "Select themes:",
        ["AI", "Healthcare", "Education", "Finance", "E-commerce", "Agriculture", "Tourism", "Entertainment", "Energy", "Real Estate", "Transportation"]
    )
    user_input = ", ".join(keywords)
else:
    user_input = st.text_area("Describe the problem you're trying to solve:")

# Generate button
if st.button("Generate Startup Idea"):
    if not user_input.strip():
        st.warning("Please provide input before generating!")
    else:
        with st.spinner('Generating your startup idea...'):
            prompt = f"""
            You are an expert startup mentor. Based on the following input: "{user_input}", generate a detailed startup plan including:

            1. Startup Name
            2. One-Liner Description
            3. Problem Statement
            4. Target Market
            5. Solution Overview
            6. Business Model
            7. Marketing Strategy
            8. Potential Challenges
            9. Next Steps

            Respond in well-structured Markdown format.
            """

            model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
            response = model.generate_content(prompt)

            st.markdown(response.text)

st.markdown("---")
st.markdown("Developed by Asim Raza")
