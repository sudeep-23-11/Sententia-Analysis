import streamlit as st
from urlextract import URLExtract

def get_total (data, user) :

    if user == "All users" :
        df = data
    else :
        df = data[(data["user"] == user)]

    messages = df["message"].tolist()

    words = []
    for i in df["message"] :
        words.extend(i.split())

    media = df[(df["message"] == "<Media omitted>\n")]

    extractor = URLExtract()
    links = []
    for i in df["message"] :
        links.extend(extractor.find_urls(i))

    c1, c2, c3, c4 = st.columns(spec=[1, 1, 1,  1], gap="small")
    with c1:
        st.header("Total Messages typed")
        st.subheader(len(messages))
    with c2:
        st.header("Total Words used")
        st.subheader(len(words))
    with c3:
        st.header("Total Media shared")
        st.subheader(media.size)
    with c4:
        st.header("Total Links shared")
        st.subheader(len(links))
    st.write('#')