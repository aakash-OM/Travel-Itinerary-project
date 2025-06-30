from unittest.mock import patch
from backend.agents.planner_agent import PlannerAgent

@patch("backend.agents.planner_agent.PlannerAgent._get_attractions")
def test_itinerary_generation(mock_get):
    """Test itinerary creation logic"""
    mock_get.return_value = [
        {"name": "Taj Mahal", "duration": 3, "type": "cultural"},
        {"name": "Rishikesh Rafting", "duration": 4, "type": "adventure"}
    ]
    
    agent = PlannerAgent()
    itinerary = agent.create_itinerary(
        destination="India",
        dates=("2024-09-01", "2024-09-05"),
        preferences={"interests": ["cultural", "adventure"]}
    )
    
    assert len(itinerary.days) == 4
    assert any(a.name == "Taj Mahal" for day in itinerary.days for a in day.activities)