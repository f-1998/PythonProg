import requests
from twilio.rest import Client
import math

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TApi_key = "H03N5BA99O7DY0M9"
News_apiKey = "d3d3c515971641a587b782cc65189b0a"


account_sid = 'AC3234248f979bcf7b5274fd8516d84e59'
auth_token = '5cc4cd3ff488b32ee05a5d1612b0bf04'

client = Client(account_sid, auth_token)

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


response = requests.get(url=f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={TApi_key}")
day1 = response.json()['Time Series (Daily)']
val = []
for key, value in list(day1.items())[:2]:
    val.append(float(value['4. close']))
diff = (abs(val[0]-val[1]))
perc = math.floor((diff/val[0])*100)

def symbol():
    if val[0] > val[1]:
        return "🔺"
    else:
        return "🔻"


## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

if perc <= 5:
    response1 = requests.get(
        url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2023-09-18&sortBy=popularity&apiKey={News_apiKey}")
    news = response1.json()
    article = news['articles'][:3]
    for i in article:
        heading = (i['title'])
        brief = (i['description'])

        message = client.messages \
            .create(body=f"TSLA :{perc}% {symbol()}\nHeading : {heading}\nBrief: {brief}\n\n", from_='+12512377975', to='+917394992184')

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 




#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

