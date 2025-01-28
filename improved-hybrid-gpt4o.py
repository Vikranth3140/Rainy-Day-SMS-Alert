import json
import os
import logging
import requests
import schedule
import time
from smsapi.client import SmsApiPlClient

# Setup logging
logging.basicConfig(
    filename="weather_alert.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Load environment variables
SMSAPI_TOKEN = os.getenv('SMSAPI_TOKEN')
OPENWEATHER_APPID = os.getenv('OPENWEATHER_APPID')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
LAT = os.getenv('LATITUDE', '51.5074')  # Default to London if not set
LON = os.getenv('LONGITUDE', '-0.1278')  # Default to London if not set
CHECK_INTERVAL_MINUTES = 30  # Frequency to check weather (in minutes)

# Initialize SMSAPI client
client = SmsApiPlClient(access_token=SMSAPI_TOKEN)

# Function to check weather and send SMS
def check_weather_and_alert():
    try:
        # Fetch weather data
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={OPENWEATHER_APPID}"
        response = requests.get(weather_url)
        response.raise_for_status()
        weather_data = response.json()

        # Get weather ID and description
        if 'weather' not in weather_data or not weather_data['weather']:
            logging.warning("No weather data available.")
            return

        weather_id = weather_data['weather'][0]['id']
        weather_description = weather_data['weather'][0]['description']
        temp_c = weather_data['main']['temp'] - 273.15  # Convert temperature to Celsius

        # Check for rain-related conditions (weather IDs: 500-599)
        if 500 <= weather_id < 600:
            message = (
                f"Rain alert: {weather_description}. "
                f"Temp: {temp_c:.1f}°C. Bring an umbrella!"
            )

            # Send SMS
            try:
                client.sms.send(to=PHONE_NUMBER, message=message)
                logging.info(f"SMS sent: {message}")
            except Exception as sms_error:
                logging.error(f"Failed to send SMS: {sms_error}")
        else:
            logging.info("No rain forecasted. SMS not sent.")

    except requests.exceptions.RequestException as api_error:
        logging.error(f"API Error: {api_error}")

# Schedule the function
schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(check_weather_and_alert)

# Run the scheduler
logging.info("Starting weather alert service...")
while True:
    schedule.run_pending()
    time.sleep(1)
