import requests
from utils.config import settings

def get_weather_forecast(location: str, days: int) -> dict:
    """Gets weather forecast for a location"""
    try:
        response = requests.get(
            "https://api.weatherapi.com/v1/forecast.json",
            params={
                "key": settings.weather_api_key,
                "q": location,
                "days": days,
                "aqi": "no",
                "alerts": "no"
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}