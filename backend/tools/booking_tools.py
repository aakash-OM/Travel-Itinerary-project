import requests
import os
from urllib.parse import urlencode
from utils.logger import logger

def generate_affiliate_link(base_url: str, params: dict, user_id: str) -> str:
    """Generates affiliate link with tracking"""
    affiliate_id = os.getenv("AFFILIATE_ID", "travelgenius123")
    params["affiliate_id"] = affiliate_id
    params["user_ref"] = user_id
    return f"{base_url}?{urlencode(params)}"

def search_flights(origin: str, destination: str, date: str) -> list:
    """Searches flights using Skyscanner API"""
    try:
        url = "https://partners.api.skyscanner.net/apiservices/browsequotes/v1.0"
        headers = {"X-API-Key": os.getenv("SKYSCANNER_KEY")}
        params = {
            "country": "US",
            "currency": "USD",
            "locale": "en-US",
            "originPlace": f"{origin}-sky",
            "destinationPlace": f"{destination}-sky",
            "outboundDate": date
        }
        response = requests.get(f"{url}/US/USD/en-US/{origin}/{destination}/{date}", 
                               headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("Quotes", [])
    except Exception as e:
        logger.error(f"Flight search failed: {str(e)}")
        return []

# Similar functions for hotels, trains, activities