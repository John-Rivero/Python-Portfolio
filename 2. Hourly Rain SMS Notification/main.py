import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OpenWeatherMap_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
latitude = 33.197960
longitude = -96.615021
exclude = 'current,minutely,daily'

api_key = os.getenv('api_key')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')


parameters = \
    {
        'lat' : latitude,
        'lon' : longitude,
        'exclude' : exclude,
        'appid' : api_key,
    }
    
response = requests.get(OpenWeatherMap_endpoint, params=parameters)

weather_data = response.json()
twelve_hours = weather_data['hourly'][0:12]


# for twelve in twelve_hours:
#     print(twelve['weather'][0]['id'])

will_rain = False

for n in range(12):
    hourly_weather = weather_data['hourly'][n]['weather'][0]['id']
    if int(hourly_weather) < 700:
        rain = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today.",
                        from_='+18559284034',
                        to='+1 817 760 8212'
                    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's Sunny today.",
                        from_='+18559284034',
                        to='+1 817 760 8212'
                    )
                    
print(message.status)