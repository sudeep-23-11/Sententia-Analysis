import streamlit as st

import preprocessing
from statistical import total
from statistical import most
from statistical import timeline

with st.sidebar :
    st.title("WhatsApp Chat Analyzer")
    file = st.file_uploader(label="Choose a file", type=["txt"], accept_multiple_files=False)

if file :
    data = file.getvalue().decode("utf-8")
    df = preprocessing.preprocessor(data)

    unique_users = df["user"].unique().tolist()
    unique_users.remove("WhatsApp Notifications")
    unique_users.sort()
    unique_users.insert(0, "All users")
    with st.sidebar :
        user = st.selectbox(label="Choose a user", options=unique_users, index=0)
        stat = st.button(label="Statistical Analysis", type="primary")
        senti = st.button(label="Sentimental Analysis", type="primary")

    if stat :
        total.get_total(df, user)
        most.get_most(df, user)
        timeline.get_timeline(df, user)