import streamlit as st
import matplotlib.pyplot as plt

def get_timeline (data, user) :

    if user == "All users" :
        df = data
    else :
        df = data[(data["user"] == user)]

    year = df.groupby(["year"])["message"].count()
    fig1, ax = plt.subplots()
    ax.plot(year.index, year.values, color='b')
    plt.xlabel("Year")
    plt.ylabel("Frequency")

    month = df.groupby(["month"])["message"].count()
    fig2, ax = plt.subplots()
    ax.plot(month.index, month.values, color='g')
    plt.xlabel("Month")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)

    c1, c2 = st.columns(spec=[1, 1], gap="small")
    with c1:
        st.header("Yearly timeline")
        st.pyplot(fig1)
    with c2:
        st.header("Monthly timeline")
        st.pyplot(fig2)

    day = df.groupby(["day"])["message"].count()
    fig1, ax = plt.subplots()
    ax.plot(day.index, day.values, color='m')
    plt.xlabel("Day")
    plt.ylabel("Frequency")

    hour = df.groupby(["hour"])["message"].count()
    fig2, ax = plt.subplots()
    ax.plot(hour.index, hour.values, color='c')
    plt.xlabel("Hour")
    plt.ylabel("Frequency")

    c1, c2 = st.columns(spec=[1, 1], gap="small")
    with c1:
        st.header("Daily timeline")
        st.pyplot(fig1)
    with c2:
        st.header("Hourly timeline")
        st.pyplot(fig2)