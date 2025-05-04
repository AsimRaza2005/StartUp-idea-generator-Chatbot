import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini via LangChain
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest", google_api_key=api_key)

# Streamlit page config
st.set_page_config(page_title="Start-Up Idea Generator", page_icon=":bulb:")
st.title("Start Your Startup Journey!")
st.subheader("Input your ideas and generate a complete startup plan.")

# Input type selection
input_mode = st.radio("Choose your input method:", ("Keywords", "Problem Statement"))

if input_mode == "Keywords":
    keywords = st.multiselect(
        "Select themes:",
        ["AI", "Healthcare", "Education", "Finance", "E-commerce", "Agriculture", "Tourism",
         "Entertainment", "Energy", "Real Estate", "Transportation"]
    )
    user_input = ", ".join(keywords)
else:
    user_input = st.text_area("Describe the problem you're trying to solve:")

# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["idea"],
    template="""
    You are an expert startup mentor. Based on the following input: "{idea}", generate a detailed startup plan including:

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
)

# LangChain LLMChain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Button logic
if st.button("Generate Startup Idea"):
    if not user_input.strip():
        st.warning("Please provide input before generating!")
    else:
        with st.spinner('Generating your startup idea...'):
            result = chain.run(idea=user_input)
            st.markdown(result)

st.markdown("---")
st.markdown("Developed by Asim Raza")
