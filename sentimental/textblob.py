import streamlit as st
import matplotlib.pyplot as plt
from textblob import TextBlob

def get_textblob (data, user) :

    if user == "All users" :
        df = data
    else :
        df = data[(data["user"] == user)]

    pos = 0
    neg = 0
    neu = 0
    for m in df["message"] :
        analyzer = TextBlob(m)
        senti = analyzer.sentiment.polarity
        if senti>0 :
            pos+=1
        elif senti<0 :
            neg+=1
        else :
            neu+=1

    fig, ax = plt.subplots()
    ax.bar(["Positive"], pos, color='g')
    ax.bar(["Neutral"], neu, color='k')
    ax.bar(["Negative"], neg, color='r')
    plt.xlabel("Class")
    plt.ylabel("Frequency")
    c1, c2 = st.columns(spec=[1, 1], gap="small")
    with c1:
        st.header("Using Text Blob")
        st.pyplot(fig)
    st.write('#')