import datetime as dt
import pandas as pd
import smtplib as sl
from random import choice

three_letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
selected_file = choice(three_letters)
letter_to_send = ""

df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict("records")

now = dt.datetime.now()
tdate = now.day
tmonth = now.month

guy_list = [x["name"] for x in birthdays if int(x["month"]) == tmonth and int(x["day"]) == tdate]
guy = ''.join(guy_list)

with open(file=selected_file, mode="r") as file:
    content = file.read()
    content = content.replace('[NAME]', guy)

with open(file="Birthday_letter.txt", mode="w") as file:
    file.write(content)

with sl.SMTP("smtp-mail.outlook.com", 587) as connection:
    connection.starttls()
    connection.login(user="pythontest122@outlook.com", password="knsp2793")
    connection.sendmail(
        from_addr="pythontest122@outlook.com",
        to_addrs="aadi2399@outlook.com",
        msg=f"Subject:Happy Birthday\n\n{letter_to_send}"
    )

