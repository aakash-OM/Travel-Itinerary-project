from pydantic import BaseModel
from datetime import date
from typing import Optional

class TripRequest(BaseModel):
    destination: str
    start_date: date
    end_date: date
    preferences: dict
    include_story: bool = True

class BookingRequest(BaseModel):
    user_id: str
    itinerary: dict  # Would reference Itinerary model
    payment_token: str

class StoryRequest(BaseModel):
    destination: str
    format: Optional[str] = "video"  # "video", "ar", "text"

class ContextRequest(BaseModel):
    destination: str
    dates: tuple[date, date]