from unittest.mock import patch
from backend.services.analytics_service import track_affiliate_click

@patch("backend.services.analytics_service.client.query")
def test_affiliate_tracking(mock_query):
    """Test affiliate click tracking"""
    track_affiliate_click("user123", "skyscanner", "Paris")
    mock_query.assert_called_once()