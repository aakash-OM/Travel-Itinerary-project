from unittest.mock import patch
from backend.tools.event_tools import get_holidays, get_local_events

@patch("backend.tools.event_tools.requests.get")
def test_holiday_fetching(mock_get):
    """Test holiday API response parsing"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"name": "New Year's Day"}]
    
    holidays = get_holidays("US", 2024)
    assert any(h["name"] == "New Year's Day" for h in holidays)

@patch("backend.tools.event_tools.requests.get")
def test_event_search(mock_get):
    """Test local event retrieval"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"results": [{"title": "Music Festival"}]}
    
    events = get_local_events("Berlin", "2024-07-15")
    assert events[0]["title"] == "Music Festival"