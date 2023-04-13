import streamlit as st
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_vader (data, user) :

    if user == "All users" :
        df = data
    else :
        df = data[(data["user"] == user)]

    analyzer = SentimentIntensityAnalyzer()
    pos = 0
    neg = 0
    neu = 0
    for m in df["message"] :
        senti = analyzer.polarity_scores(m)
        if senti["pos"] > senti["neg"] and senti["pos"] > senti["neu"] :
            pos+=1
        elif senti["neg"] > senti["pos"] and senti["neg"] > senti["neu"] :
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
        st.header("Using Vader")
        st.pyplot(fig)
    st.write('#')