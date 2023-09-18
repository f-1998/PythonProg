import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day = now.weekday()
if day == 4:
    my_email = "abc@gmail.com" #your email
    password = "abc 89jsdch" #your password

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        with open("quotes.txt", "r") as file:
            line = random.choice(file.readlines())
            connection.sendmail(from_addr=my_email, to_addrs="xyz@hotmail.com", msg=f"Subject: Quote\n\n{line}")

