from fastapi import APIRouter
from services.orchestration import TravelOrchestrator

router = APIRouter()

@router.post("/plan")
async def plan_trip(request: TripRequest):
    orchestrator = TravelOrchestrator()
    itinerary = orchestrator.create_itinerary(
        destination=request.destination,
        dates=request.dates,
        preferences=request.preferences
    )
    
    if request.include_story:
        itinerary.story = orchestrator.generate_story(request.destination)
    
    return itinerary

@router.post("/book")
async def book_trip(request: BookingRequest):
    booker = BookerAgent()
    return {
        'flights': booker.book_flight(request.user, request.itinerary),
        'hotels': booker.book_hotel(request.user, request.itinerary)
    }