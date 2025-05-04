import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

# Configure Gemini API Key
api_key = st.secrets["GOOGLE_API_KEY"]

# Streamlit UI Setup
st.set_page_config(page_title="Start-Up Idea Generator", page_icon=":bulb:")
st.title("Start Your Startup Journey!")
st.subheader("Input your ideas and generate a complete startup plan.")

# User Input
input_mode = st.radio("Choose your input method:", ("Keywords", "Problem Statement"))

if input_mode == "Keywords":
    keywords = st.multiselect(
        "Select themes:",
        ["AI", "Healthcare", "Education", "Finance", "E-commerce", "Agriculture", "Tourism", "Entertainment", "Energy", "Real Estate", "Transportation"]
    )
    user_input = ", ".join(keywords)
else:
    user_input = st.text_area("Describe the problem you're trying to solve:")

# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["input"],
    template="""
You are an expert startup mentor. Based on the following input: "{input}", generate a detailed startup plan including:

1. **Startup Name**
2. **One-Liner Description**
3. **Problem Statement**
4. **Target Market**
5. **Solution Overview**
6. **Business Model**
7. **Marketing Strategy**
8. **Potential Challenges**
9. **Next Steps**

Respond in well-structured **Markdown** format.
"""
)

# Setup LangChain Components
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
chain = LLMChain(llm=llm, prompt=prompt_template, output_parser=StrOutputParser())

# Generate Button
if st.button("Generate Startup Idea"):
    if not user_input.strip():
        st.warning("Please provide input before generating!")
    else:
        with st.spinner("Generating your startup idea..."):
            result = chain.run({"input": user_input})
            st.markdown(result)

st.markdown("---")
st.markdown("Developed by Asim Raza")
