from langchain.tools import tool
import requests
from datetime import datetime, timedelta
from models.itinerary import Destination
from utils.logger import logger

class ContextAgent:
    def __init__(self):
        self.weather_api = "https://api.weatherapi.com/v1/forecast.json"
        self.events_api = "https://api.predicthq.com/v1/events/"
    
    @tool("Get Travel Context")
    def get_travel_context(self, destination: Destination, dates: tuple) -> dict:
        """Provides weather, events, and advisories for a destination"""
        try:
            # Get weather forecast
            weather = self._get_weather(destination, dates)
            
            # Check for local events
            events = self._get_events(destination, dates[0])
            
            # Get travel advisories
            advisories = self._get_advisories(destination.country_code)
            
            return {
                'weather': weather,
                'events': events,
                'advisories': advisories
            }
        except Exception as e:
            logger.error(f"Context error: {str(e)}")
            return {"error": "Failed to fetch context data"}

    def _get_weather(self, destination, dates):
        params = {
            'key': os.getenv("WEATHERAPI_KEY"),
            'q': destination.coordinates or destination.name,
            'days': (dates[1] - dates[0]).days
        }
        response = requests.get(self.weather_api, params=params)
        response.raise_for_status()
        return response.json().get('forecast', {}).get('forecastday', [])
    
    def _get_events(self, destination, start_date):
        headers = {"Authorization": f"Bearer {os.getenv('PREDICTHQ_KEY')}"}
        params = {
            'q': destination.name,
            'start': f"{start_date}T00:00:00",
            'limit': 5
        }
        response = requests.get(self.events_api, headers=headers, params=params)
        return response.json().get('results', [])
    
    def _get_advisories(self, country_code):
        # Would integrate with travel advisory API
        return {"level": 1, "message": "Normal precautions"}