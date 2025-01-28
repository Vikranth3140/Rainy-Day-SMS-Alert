import json
import os
import requests
from smsapi.client import SmsApiPlClient

# Load environment variables
SMSAPI_TOKEN = os.getenv('SMSAPI_TOKEN')
OPENWEATHER_APPID = os.getenv('OPENWEATHER_APPID')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
LAT = 51.5074  # Replace with your latitude
LON = -0.1278  # Replace with your longitude

# Initialize SMSAPI client
client = SmsApiPlClient(access_token=SMSAPI_TOKEN)

# Fetch weather data
weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={OPENWEATHER_APPID}'

try:
    response = requests.get(weather_url)
    response.raise_for_status()
    weather_data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
    exit()

# Check for rain using weather ID (500-599 = rain)
if 'weather' not in weather_data or not weather_data['weather']:
    print("No weather data available.")
    exit()

weather_id = weather_data['weather'][0]['id']
if 500 <= weather_id < 600:
    # Optional: Add temperature data
    temp_c = weather_data['main']['temp'] - 273.15
    message = (
        f"Rain alert: {weather_data['weather'][0]['description']}. "
        f"Temp: {temp_c:.1f}°C. Bring an umbrella!"
    )
    
    # Send SMS
    try:
        client.sms.send(to=PHONE_NUMBER, message=message)
        print("SMS sent successfully!")
    except Exception as e:
        print(f"SMS failed: {e}")