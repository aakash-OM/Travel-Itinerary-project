from unittest.mock import MagicMock, patch
from backend.services.orchestration import TravelOrchestrator
from backend.models.itinerary import Itinerary

@patch("backend.services.orchestration.PlannerAgent")
@patch("backend.services.orchestration.ContextAgent")
def test_itinerary_creation(mock_context, mock_planner):
    """Test full itinerary generation flow"""
    # Setup mock agents
    mock_planner.return_value.create_itinerary.return_value = Itinerary(
        destination="Kyoto",
        start_date="2024-11-01",
        end_date="2024-11-05"
    )
    mock_context.return_value.get_travel_context.return_value = {
        "weather": "sunny",
        "events": ["Cultural Festival"]
    }
    
    # Execute orchestration
    orchestrator = TravelOrchestrator()
    itinerary = orchestrator.create_itinerary(
        destination="Kyoto",
        dates=("2024-11-01", "2024-11-05"),
        preferences={"interests": ["cultural"]}
    )
    
    assert itinerary.destination == "Kyoto"
    assert "Cultural Festival" in itinerary.context["events"]