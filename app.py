import streamlit as st
from preprocessing import preprocessor

with st.sidebar :
    st.title("WhatsApp Chat Analyzer")
    file = st.file_uploader(label="Choose a file", type=["txt"], accept_multiple_files=False)

if file :
    data = file.getvalue().decode("utf-8")
    df = preprocessor(data)