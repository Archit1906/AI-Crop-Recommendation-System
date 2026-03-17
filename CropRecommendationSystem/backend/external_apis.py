import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str):
    """
    Fetches real-time temperature and humidity from OpenWeather API for a given city.
    """
    if not OPENWEATHER_API_KEY:
        return {"error": "OpenWeather API key not configured"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
