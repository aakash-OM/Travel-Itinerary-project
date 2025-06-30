import pytest
from unittest.mock import patch
from backend.tools.weather_tool import get_weather_forecast

@patch("backend.tools.weather_tool.requests.get")
def test_get_weather_success(mock_get):
    """Test successful weather API response"""
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "forecast": {"forecastday": [{"day": {"maxtemp_c": 25}}]}
    }
    
    result = get_weather_forecast("Paris", 3)
    assert "forecast" in result
    assert result["forecast"]["forecastday"][0]["day"]["maxtemp_c"] == 25

@patch("backend.tools.weather_tool.requests.get")
def test_get_weather_failure(mock_get):
    """Test API failure handling"""
    mock_response = mock_get.return_value
    mock_response.status_code = 500
    
    result = get_weather_forecast("InvalidLocation", 3)
    assert "error" in result