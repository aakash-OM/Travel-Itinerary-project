from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Activity(BaseModel):
    name: str
    type: str  # e.g., "adventure", "cultural"
    start_time: str
    end_time: str
    location: str
    description: Optional[str] = None
    cost: Optional[float] = None

class DayPlan(BaseModel):
    date: date
    activities: List[Activity]

class Itinerary(BaseModel):
    destination: str
    start_date: date
    end_date: date
    days: List[DayPlan] = []
    story: Optional[dict] = None  # For destination story
    context: Optional[dict] = None  # Weather/events context