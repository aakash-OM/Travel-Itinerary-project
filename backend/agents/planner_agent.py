from crewai import Agent
from langchain.tools import tool
from models.itinerary import Itinerary

class PlannerAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Senior Travel Planner',
            goal='Create optimized itineraries based on user preferences',
            tools=[self._get_attractions],
            verbose=True
        )
    
    @tool("Search Attractions")
    def _get_attractions(location: str, preferences: dict) -> list:
        """Find attractions matching user preferences"""
        # Implementation using Google Places API
        return []
    
    def create_itinerary(self, destination, dates, preferences):
        attractions = self._get_attractions(destination, preferences)
        return Itinerary(
            destination=destination,
            dates=dates,
            activities=self._optimize_schedule(attractions, dates)
        )