from pydantic import BaseModel
from typing import List, Optional

class TravelPreferences(BaseModel):
    budget: float
    interests: List[str]  # e.g., ["adventure", "cultural"]
    pace: str  # "relaxed", "moderate", "intense"
    accessibility_needs: Optional[List[str]] = None
    dietary_restrictions: Optional[List[str]] = None

class PaymentMethod(BaseModel):
    token: str  # Payment provider token
    type: str   # "credit_card", "paypal", etc.
    last_four: Optional[str] = None

class UserProfile(BaseModel):
    user_id: str
    name: str
    email: str
    home_location: str
    travel_preferences: TravelPreferences
    payment_methods: List[PaymentMethod] = []