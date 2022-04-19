import os
from sqlite3 import paramstyle
from pip._vendor import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('APIKEY')
account_sid ="AC122318ff1fa0b0d4ebffcc9dae6c881d"
auth_token =os.getenv('AUTH')

# CITY="Chennai,India"
MY_LAT =-12.977749
MY_LON =-38.501629



parameters={
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid": API_KEY,
    "exclude":"current,minutely,daily"
}


response= requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data= response.json()
hourly_data= data["hourly"]


will_rain = False

for i in  hourly_data:
    weather_hourly=i["weather"][0]["id"]
    if weather_hourly<700:
        will_rain=True

if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages \
        .create(
        body="It is going to rain today, Remember to bring an umberella ",
        from_='+13186071322',
        to='+916303344156'
        )
print(message.status)             
    