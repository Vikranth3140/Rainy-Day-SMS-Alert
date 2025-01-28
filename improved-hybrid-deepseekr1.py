import json
import os
import requests
import logging
import schedule
import time
from smsapi.client import SmsApiPlClient
from dotenv import load_dotenv  # Optional for .env support

# Load environment variables
load_dotenv()  # Remove if not using .env file
SMSAPI_TOKEN = os.getenv("SMSAPI_TOKEN")
OPENWEATHER_APPID = os.getenv("OPENWEATHER_APPID")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
LAT = os.getenv("LAT")  # Validate as float later
LON = os.getenv("LON")  # Validate as float later
CHECK_INTERVAL_MINUTES = 30

# Configure logging
logging.basicConfig(
    filename="weather_alert.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Initialize SMS client
client = SmsApiPlClient(access_token=SMSAPI_TOKEN)

def check_weather_and_alert():
    try:
        # Fetch weather data
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={OPENWEATHER_APPID}"
        response = requests.get(weather_url)
        response.raise_for_status()
        weather_data = response.json()
        
        # Validate response
        if "weather" not in weather_data or not weather_data["weather"]:
            logging.error("No weather data in response")
            return

        # Check for rain using weather ID (500-599 = rain)
        weather_id = weather_data["weather"][0]["id"]
        if 500 <= weather_id < 600:
            # Optional: Add temperature
            temp_c = weather_data["main"]["temp"] - 273.15
            message = (
                f"Rain alert: {weather_data['weather'][0]['description']}. "
                f"Temp: {temp_c:.1f}°C. Bring an umbrella!"
            )
            
            # Send SMS
            client.sms.send(to=PHONE_NUMBER, message=message)
            logging.info(f"SMS sent: {message}")
        else:
            logging.info("No rain detected")

    except requests.exceptions.RequestException as e:
        logging.error(f"API Request Failed: {e}")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")

# Schedule and run
schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(check_weather_and_alert)
logging.info("Weather alert service started")

while True:
    schedule.run_pending()
    time.sleep(1)