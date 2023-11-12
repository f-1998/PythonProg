from bs4 import BeautifulSoup
import requests
import re
import smtplib
from twilio.rest import Client


account_sid = 'TWILIO_SID' #twilio sid
auth_token = 'TWILIO_AUTH_TOKEN' #twilio auth_token

LINK = "https://www.amazon.in/gp/aw/d/B09DFM5PQT/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=926b790cdc402a589950280d675f2cde&hsa_cr_id=0&qid=1699694570&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&ref_=sbx_be_s_sparkle_mcd_asin_0_img&pd_rd_w=U2baI&content-id=amzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d%3Aamzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_p=df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_r=P94D98KT1APRN7CVQJ4C&pd_rd_wg=JtG7e&pd_rd_r=3c9c967b-dea1-4949-ac2e-52839434dbfd"
response = requests.get(LINK, headers={"User-Agent": "Defined"}).text
soup = BeautifulSoup(response, "html.parser")

price_span = soup.find(name="span", class_='a-price-whole')
price_s = price_span.text
price = int(re.sub(r'[,.]', "", price_s))

my_email = "example@gmail.com" #youremail
password = "123abc 123abc asb" #yourapppassword

if price < 35000:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='example@hotmail.com', #Receiver email address
                            msg=f"Subject: Amazon Price Alert:\n\n Your Product price has dropped to {price}")

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Amazon Price Alert:\n\n Your Product price has dropped to {price}",
        from_='+1234567890',  # Twilio phone number
        to='+1234567890' # receiver phone number verified
    )

    print(message.sid)


