import requests
import os
from datetime import date
from dotenv import load_dotenv
from pushover import Pushover

load_dotenv()

current_date = date.today()
formatted_date = current_date.strftime("%Y-%m-%d")


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

#ENDPOINTS
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
function = "TIME_SERIES_DAILY_ADJUSTED"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


#APIs
stock_api = os.getenv('STOCK_PRICE_API')
news_api = os.getenv("NEWS_API")
pushover_api = os.getenv("PUSHOVER_API")
pushover_user = os.getenv("PUSHOVER_USER")




stock_parameters = \
    {
        'function' : function,
        'symbol' : STOCK_NAME,
        'apikey' : stock_api
        
    }

news_parameters = \
    {
        'apiKey' : news_api,
        'qInTitle' : COMPANY_NAME,
        
    }
    
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()


news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news = news_response.json()['articles']



#This is to get the price for opening and closing
daily = stock_data['Time Series (Daily)']
open_stock = float(list(daily.values())[0]['1. open'])
close_stock = float(list(daily.values())[1]['4. close'])



#Identify the percent difference between the closing the day before and the opening for the current day.
percent_difference = round(abs((open_stock-close_stock) / open_stock) * 100, 2)
if (open_stock-close_stock) < 0:
    sign = '-'
    
elif (open_stock-close_stock) > 0:
    sign = '+'

#***********NEWS*****************

for n in range(4):
    if n != 1:
        
        three_news = news[n]
    
        title = three_news['title']
        description = three_news['description']
        
        if percent_difference < 5:
        
            po = Pushover(pushover_api)
            po.user(pushover_user)
            msg = po.msg(f"{STOCK_NAME}: {sign}{percent_difference}%\nCurrent Day's Opening Price: {open_stock}\nPrevious Day's Closing Price: {close_stock}\n Title: {title}\nBrief: {description}")
            po.send(msg)
            
            print(f"{STOCK_NAME}: {sign}{percent_difference}%\nCurrent Day's Opening Price: {open_stock}\nPrevious Day's Closing Price: {close_stock}\n Title: {title}\nBrief: {description}")