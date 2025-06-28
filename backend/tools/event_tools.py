import requests
from datetime import datetime
from utils.config import settings

def get_holidays(country_code: str, year: int) -> list:
    """Gets public holidays for a country"""
    response = requests.get(
        f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    )
    return response.json() if response.status_code == 200 else []

def get_local_events(location: str, date: str) -> list:
    """Gets local events from PredictHQ API"""
    headers = {"Authorization": f"Bearer {settings.predicthq_key}"}
    params = {
        "q": location,
        "start": f"{date}T00:00:00",
        "end": f"{date}T23:59:59",
        "limit": 5
    }
    response = requests.get(
        "https://api.predicthq.com/v1/events/", 
        headers=headers, 
        params=params
    )
    return response.json().get("results", []) if response.status_code == 200 else []