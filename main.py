import smtplib
import datetime as dt
import random
import pandas as pd
date_data = pd.read_csv("birthday.csv")
birthdate = (date_data["date"][0]).split("-")
to_address = []
to_person = []

date_of_today = dt.datetime.now()
month = str(date_of_today.month)
day = str(date_of_today.day)
today_list= [day, month]

birthday_list = []


my_email =# email-id from which you want to send the email
password =#Password of the above email ID

data = pd.read_csv("birthday.csv")
for x in data["date"]:
    birthday_list.append(x.split("-")[:2])


for i in range(0, len(birthday_list)):
    if birthday_list[i] == today_list:
        to_address.append(date_data["email"][i])
        to_person.append(date_data["person"][i])



for i in range (0,len(to_address)):
    random_letter_number = random.randint(1, 3)
    with open(f"Wishes{random_letter_number}.txt") as file:
        wish = file.read()
        wish = wish.replace("[Person]", to_person[i])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=#same email as above
                              ,password=# same password as above)
            connection.sendmail(from_addr=my_email,to_addrs=to_address[i],
                                msg=f"Subject: Happy Birthday.\n\n {wish}")

