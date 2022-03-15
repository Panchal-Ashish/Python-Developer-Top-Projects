import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
# ▲▼
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "PV5T197N5V69GTX9"
NEWS_API_KEY = "38ab674a9565476db8ca3d58e2f7e159"

account_sid = 'AC2859004428bce7afcad28175bb8e4d98'  # twilio
auth_token = 'cbcb1221265a2c170eec585158537556' # twilio
"Ygfm9m4ToQoxnFNpQfC7ptYI7_DrxiJG4mnixd3g"
"If you lose your phone, or don't have access to your verification device, this code is your failsafe to access your account."

UP_DOWN = None
## ----------STEP 1: Use https://www.alphavantage.co/documentation/#daily----------
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
## printing response.json()---- we get dict with 2 keys... metadata (company info) and time series daily (daily prices info)
## tapping into time series daily---- we get dict with date as key and high, low, start, close prices as value.

data = response.json()["Time Series (Daily)"]
print(data)
# print("\n")

## since we have dates as keys... it becomes hard coded as if we want yesterdays data... every day the date change so not feasible
## so using list comprehension... adding all the values in the list... each value is a dict in itself... so that they are easily accessible using indexing
data_list = [value for (key, value) in data.items()]
print(data_list)
print("\n")

###TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = float(yesterdays_data['4. close'])  ## str to float for calculations
print(f"yesterday price {yesterdays_closing_price}")

###TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])     ## str to float for calculations
print(f"day before yesterday price {day_before_yesterday_closing_price}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterdays_closing_price - day_before_yesterday_closing_price
print(f"difference = {difference}")
if difference < 0:
    UP_DOWN = "▼"
elif difference > 0:
    UP_DOWN = "▲"
elif difference == 0:
    UP_DOWN = "="

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percent = round(abs(difference) / yesterdays_closing_price * 100 , 2 )
print(f"difference percent = {difference_percent}%")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(difference_percent) >= 0.5:
    # print("get news")


## ------------------STEP 2: https://newsapi.org/ ----------------
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME   # keyword to search
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    # print(articles)
    # print("\n")

#TODO 7. - Use Python slice operator to create a list that contains the first 2 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    top_three_articles = articles[:3]
    # print(top_three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME} {UP_DOWN} {difference_percent}%\n" \
                          f"Headline: {article['title']} \n " \
                          f"Brief: {article['description']}\n" \
                          f"{article['url']}" for article in top_three_articles]
    # print(formatted_articles)
    # print("\n")
    client = Client(account_sid, auth_token)
    # for article in top_three_articles:
    #     title = article['title']
    #     description = article['description']
    #     message = client.messages.create \
    #             (
    #             body=f"{STOCK_NAME} {UP_DOWN} {difference_percent}% \nHeadline: {title} \nBrief: {description} \n{article['url']}",
    #             from_='+18482891741',
    #             to='+917506058102'
    #         )

#TODO 9. - Send each article as a separate message via Twilio.

    for article in formatted_articles:
        message = client.messages.create\
                (
            body= article,
            from_='+18482891741',
            to='+917506058102'
        )

        # print(message.sid)
        # print(message.status)

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

