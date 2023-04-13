import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from emoji import EMOJI_DATA
from emoji import demojize

def get_most (data, user) :

    if user == "All users" :
        df = data

        busy = df["user"].value_counts().head(10)
        fig, ax = plt.subplots()
        ax.barh(busy.index, busy.values, color='r')
        plt.xlabel("Frequency")
        plt.ylabel("User")
        c1, c2 = st.columns(spec=[1, 1], gap="small")
        with c1:
            st.header("Most busy Users")
            st.pyplot(fig)
        st.write('#')

    else :
        df = data[(data["user"] == user)]

    words = df[(df["user"] != "WhatsApp Notifications") & (df["message"] != "<Media omitted>\n") & (df["message"] != "This message was deleted\n")]
    f = open("./data/stop-words.txt", 'r')
    stop_words = f.read()
    f.close()
    _words = []
    for i in words["message"] :
        for j in i.split() :
            if (j.lower() not in stop_words) and (j not in EMOJI_DATA) :
                _words.append(j)
    words = pd.DataFrame(Counter(_words).most_common(10))
    fig1, ax = plt.subplots()
    ax.barh(words[0], words[1], color='y')
    plt.xlabel("Frequency")
    plt.ylabel("Word")

    _emojis = []
    for i in df["message"] :
        for j in i.split() :
            if j in EMOJI_DATA :
                _emojis.append(j)
    emojis = pd.DataFrame(Counter(_emojis).most_common(10))
    fig2, ax = plt.subplots()
    ax.pie(emojis[1], labels=[demojize(e) for e in emojis[0]], autopct="%1.1f%%", startangle=90, radius=2)
    
    c1, c2 = st.columns(spec=[1, 1], gap="small")
    with c1:
        st.header("Most used Words")
        st.pyplot(fig1)
    with c2:
        st.header("Most used Emojis")
        st.pyplot(fig2)
    st.write('#')