from unittest.mock import patch
from backend.agents.context_agent import ContextAgent

@patch("backend.agents.context_agent.get_holidays")
@patch("backend.agents.context_agent.get_weather_forecast")
def test_travel_context(mock_weather, mock_holidays):
    """Test context data aggregation"""
    mock_weather.return_value = {"forecast": "sunny"}
    mock_holidays.return_value = [{"name": "National Day"}]
    
    agent = ContextAgent()
    context = agent.get_travel_context(
        destination="Singapore",
        dates=("2024-08-09", "2024-08-11")
    )
    
    assert "National Day" in [h["name"] for h in context["holidays"]]
    assert context["weather"]["forecast"] == "sunny"