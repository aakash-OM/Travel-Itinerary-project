from pydantic import BaseModel
from typing import List
from datetime import datetime

class FlightSegment(BaseModel):
    airline: str
    flight_number: str
    departure: str
    arrival: str
    departure_time: datetime
    arrival_time: datetime

class HotelBooking(BaseModel):
    name: str
    check_in: str
    check_out: str
    room_type: str
    confirmation_code: str

class BookingConfirmation(BaseModel):
    booking_id: str
    user_id: str
    flights: List[FlightSegment] = []
    hotels: List[HotelBooking] = []
    activities: List[dict] = []
    total_cost: float
    booking_time: datetime