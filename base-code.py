import json, requests
from smsapi.client import SmsApiPlClient

# SMSAPI token and client:
token = '[your sms token]'
client = SmsApiPlClient(access_token=token)

# OpenWeather data:
APPID = '[your OpenWeather APPID]'

lat = 'your latitude'
lon = 'your longitude'

weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APPID}'

w_response = requests.get(weather_url)
w_response.raise_for_status()

weatherData = json.loads(w_response.text)
weatherDescription = weatherData['weather'][0]['description']

if 'rain' in weatherDescription or 'shower' in weatherDescription:
    # send SMS:
    client.sms.send(to='your number', message='It\'s going to rain today. Remember to take an umbrella.')