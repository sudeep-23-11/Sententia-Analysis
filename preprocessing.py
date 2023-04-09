import pandas as pd
import re

def preprocessor (data) :

    reg_exp = "\d{2}/\d{2}/\d{4},\s\d{2}:\d{2}\s-\s"
    dates = re.findall(reg_exp, data)
    users_messages = re.split(reg_exp, data)[1:]
    df = pd.DataFrame({"date": dates, "user_message": users_messages})

    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y, %H:%M - ")
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month_name()
    df["year"] = df["date"].dt.year
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute
    df.drop(["date"], axis=1, inplace=True)

    reg_exp = "([\w\W]+?):\s"
    users = []
    messages = []
    for i in df["user_message"] :
        e = re.split(reg_exp, i)
        if e[1:] :
            users.append(e[1])
            messages.append(e[2])
        else :
            users.append("WhatsApp Notifications")
            messages.append(e[0])
    df.drop(["user_message"], axis=1, inplace=True)
    df["user"] = users
    df["message"] = messages

    return df