import requests
from twilio.rest import Client

api_key ="69f04e4613056b159c2761a9d9e664d2"  #your api key from weather data

account_sid = 'AC3234248f979bcf7b5274fd8516d84e59' #twilio sid
auth_token = '5cc4cd3ff488b32ee05a5d1612b0bf04' #twilio auth_token

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat=22.572645&lon=88.363892&exclude=daily,current,minutely,alerts&appid={api_key}")

not_rain = True

while not_rain:
    for i in range(12):
        data = response.json()["hourly"][i]['weather'][0]['id']
        if data < 700:
            print("Bring an umbrella")
            not_rain = False
            break

if not not_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring an Umbrella.☔",
        from_='+12512377975', #Twilio phone number
        to='+917394992184'  # receiver phone number verified
    )


