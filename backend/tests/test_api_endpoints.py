from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_full_trip_planning_flow():
    """Test complete trip planning API workflow"""
    # Step 1: Plan itinerary
    plan_response = client.post("/api/v1/plan", json={
        "destination": "Switzerland",
        "start_date": "2024-12-15",
        "end_date": "2024-12-20",
        "preferences": {
            "interests": ["adventure", "scenery"],
            "budget": 5000
        }
    })
    assert plan_response.status_code == 200
    itinerary = plan_response.json()
    
    # Step 2: Book trip
    book_response = client.post("/api/v1/book", json={
        "user_id": "test_user",
        "itinerary": itinerary,
        "payment_token": "tok_test"
    })
    assert book_response.status_code == 200
    booking = book_response.json()
    
    assert "booking_id" in booking
    assert booking["status"] == "confirmed"