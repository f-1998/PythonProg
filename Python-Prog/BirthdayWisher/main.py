

import pandas
import random
import smtplib
import datetime as dt

# 1. Update the birthdays.csv

df = pandas.read_csv('birthdays.csv',encoding='utf-8')

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
filter1 = df['month'] == now.month
filter2 = df['day'] == now.day
new = df[filter1 & filter2]

dict = {}
for index, row in new.iterrows():
    name = row['name']
    email = row['email']
    dict[name] = email

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

# 4. Send the letter generated in step 3 to that person's email address.
with open(letter_path, "r",encoding='utf-8') as file:
    letter_template = file.read()

my_email = "example@gmail.com" #youremail
password = "abc" #yourapppassword

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    for index, row in dict.items():
        recipient_name = index
        recipient_email = row
        letter = letter_template.replace("[NAME]", recipient_name)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"Subject: Birthday Wish:\n\n{letter}")


