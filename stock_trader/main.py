import requests
import time
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "6f3e0fb1db6f4f9bba72300d8f704e4b"
STOCK_API_KEY = "V7R1I2VX9N761L17"
ACCOUNT_SID = 'ACe72d733d8d71bfbdf3f874fcb41f563d'
AUTH_TOKEN = '83b9c91a862fe2f626b38c8619cb6335'

NEWS_PARAMS = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

r = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
r.raise_for_status()
stock_data = r.json()["Time Series (Daily)"]
formatted_stock_data = [val for (key, val) in stock_data.items()]
# print(formatted_stock_data)

yesterday_price = float(formatted_stock_data[0]["4. close"])
# print(yesterday_price)
day_before_yesterday_price = float(formatted_stock_data[1]["4. close"])
# print(yesterday_price, day_before_yesterday_price)
stock_change = abs(yesterday_price - day_before_yesterday_price)
# print(stock_change)
percent_change = stock_change/yesterday_price * 100
# print(percent_change)

if percent_change > 5:
    print("Get News.")
    r_news = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    r_news.raise_for_status()
    news_data = r_news.json()["articles"]
    # print(news_data)
    formatted_news_data = news_data[:3]
    print(formatted_news_data)
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in formatted_news_data]
    # Twilio

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+18884877013",
            to='+16306396125'
    )
else:
    print("Minor change.")





