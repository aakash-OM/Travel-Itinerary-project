from unittest.mock import patch
from backend.tools.booking_tools import generate_affiliate_link, search_flights

def test_affiliate_link_generation():
    """Test affiliate link formatting"""
    link = generate_affiliate_link(
        "https://booking.com", 
        {"param": "value"}, 
        "user123"
    )
    assert "affiliate_id" in link
    assert "user_ref=user123" in link

@patch("backend.tools.booking_tools.requests.get")
def test_flight_search_success(mock_get):
    """Test flight search API success"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"Quotes": [{"MinPrice": 200}]}
    
    results = search_flights("NYC", "LON", "2024-12-01")
    assert len(results) > 0
    assert results[0]["MinPrice"] == 200