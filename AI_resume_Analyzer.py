import os
import streamlit as st
from google import genai
from PyPDF2 import PdfReader

api_key =os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key=api_key)

st.title('AI Resume Analyzer')

resume = st.file_uploader('Upload Your Resume', type='pdf')

if resume:
    pdf = PdfReader(resume)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
        
    st.success('Resume Readed.')

    if st.button('Analyze Resume'):
        with st.spinner('Wait 30 sec...'):
            try:
                prompt = f"""
Analyze the Resume.
tell the missing points.
give the 30 interview questions from technical and non technical based on the resume skills.
{text}
"""
                response = client.models.generate_content(model='gemini-3.8-flash', contents=prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Error occured: {e}")