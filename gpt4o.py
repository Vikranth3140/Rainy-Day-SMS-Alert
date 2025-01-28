import json
import requests
import logging
import schedule
import time
from smsapi.client import SmsApiPlClient

# Setup logging
logging.basicConfig(
    filename="weather_alert.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Configurations
TOKEN = "your_sms_token"
APPID = "your_openweather_appid"
LAT = "your_latitude"
LON = "your_longitude"
PHONE_NUMBER = "your_phone_number"
CHECK_INTERVAL_MINUTES = 30  # Frequency to check weather (in minutes)

# Initialize SMS client
client = SmsApiPlClient(access_token=TOKEN)

# Function to check weather and send SMS
def check_weather_and_alert():
    try:
        # Fetch weather data
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APPID}"
        response = requests.get(weather_url)
        response.raise_for_status()
        weather_data = response.json()
        
        # Get weather description
        weather_description = weather_data["weather"][0]["description"]
        logging.info(f"Weather fetched: {weather_description}")

        # Check for rain-related conditions
        if "rain" in weather_description or "shower" in weather_description:
            # Send SMS
            message = "It's going to rain today. Remember to take an umbrella."
            client.sms.send(to=PHONE_NUMBER, message=message)
            logging.info(f"SMS sent: {message}")
        else:
            logging.info("No rain forecasted. SMS not sent.")

    except Exception as e:
        logging.error(f"Error: {e}")

# Schedule the function
schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(check_weather_and_alert)

# Run the scheduler
logging.info("Starting weather alert service...")
while True:
    schedule.run_pending()
    time.sleep(1)
