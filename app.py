import streamlit as st
from preprocessing import preprocessor
from total import get_total
from most import get_most

with st.sidebar :
    st.title("WhatsApp Chat Analyzer")
    file = st.file_uploader(label="Choose a file", type=["txt"], accept_multiple_files=False)

if file :
    data = file.getvalue().decode("utf-8")
    df = preprocessor(data)

    unique_users = df["user"].unique().tolist()
    unique_users.remove("WhatsApp Notifications")
    unique_users.sort()
    unique_users.insert(0, "All users")
    with st.sidebar :
        user = st.selectbox(label="Choose a user", options=unique_users, index=0)
        click = st.button(label="Show", type="primary")

    if click :
        get_total(df, user)

        get_most(df, user)
