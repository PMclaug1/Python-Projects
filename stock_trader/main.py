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

NEWS_PARAMS = {

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
print(formatted_stock_data)

yesterday_price = float(formatted_stock_data[0]["4. close"])
print(yesterday_price)
day_before_yesterday_price = float(formatted_stock_data[1]["4. close"])
print(yesterday_price, day_before_yesterday_price)
stock_change = abs(yesterday_price - day_before_yesterday_price)
print(stock_change)
percent_change = stock_change/yesterday_price * 100
print(percent_change)

if percent_change > 5:
    print("Get News.")
else:
    print("Minor change.")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

#        proxy_client = TwilioHttpClient()
#        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#        client = Client(account_sid, auth_token, http_client=proxy_client)

#        message = client.messages.create(
#            body="Bring an umbrella.",
#            from_="+18884877013",
#            to='+16306396125'
 #       )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

