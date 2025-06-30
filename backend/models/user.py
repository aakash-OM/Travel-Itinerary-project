import pytest
from unittest.mock import patch, MagicMock
from backend.tools import (
    weather_tool,
    event_tools,
    booking_tools,
    payment_tools,
    ar_tools
)

# --- Weather Tool Tests ---
@patch("backend.tools.weather_tool.requests.get")
def test_weather_tool_valid_response(mock_get):
    """Test successful weather API response"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"forecast": {"day": "sunny"}}
    
    result = weather_tool.get_weather_forecast("Paris", 3)
    assert "forecast" in result
    assert result["forecast"]["day"] == "sunny"

def test_weather_tool_invalid_days():
    """Test validation for day count"""
    with pytest.raises(ValueError):
        weather_tool.get_weather_forecast("London", -1)

# --- Event Tools Tests ---
@patch("backend.tools.event_tools.requests.get")
def test_event_tool_holiday_check(mock_get):
    """Test holiday retrieval"""
    mock_get.return_value.json.return_value = [{"name": "Republic Day"}]
    holidays = event_tools.get_holidays("IN", 2025)
    assert any("Republic" in h["name"] for h in holidays)

@patch("backend.tools.event_tools.requests.get")
def test_event_tool_api_failure(mock_get):
    """Test API failure handling"""
    mock_get.return_value.status_code = 500
    events = event_tools.get_local_events("Tokyo", "2025-04-01")
    assert events == []

# --- Booking Tools Tests ---
def test_affiliate_link_generation():
    """Test affiliate link formatting"""
    link = booking_tools.generate_affiliate_link(
        base_url="https://booking.com",
        params={"location": "Paris"},
        user_id="U123"
    )
    assert "affiliate_id=travelgenius123" in link
    assert "user_ref=U123" in link

@patch("backend.tools.booking_tools.requests.get")
def test_flight_search_success(mock_get):
    """Test successful flight search"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "Quotes": [{"MinPrice": 300}]
    }
    flights = booking_tools.search_flights("DEL", "LHR", "2025-07-01")
    assert len(flights) > 0
    assert flights[0]["MinPrice"] == 300

@patch("backend.tools.booking_tools.requests.get")
def test_flight_search_authentication_failure(mock_get):
    """Test API key failure"""
    mock_get.return_value.status_code = 401
    flights = booking_tools.search_flights("NYC", "LAX", "2025-08-15")
    assert flights == []

# --- Payment Tools Tests ---
@patch("backend.tools.payment_tools.stripe.PaymentIntent.create")
def test_payment_intent_creation(mock_create):
    """Test payment intent creation"""
    mock_create.return_value = MagicMock(
        id="pi_123",
        client_secret="secret_123",
        amount=5000,
        currency="usd"
    )
    
    intent = payment_tools.create_payment_intent(
        amount=5000,
        currency="usd",
        metadata={"trip_id": "TRP123"}
    )
    
    assert intent.id == "pi_123"
    assert intent.amount == 5000

@patch("backend.tools.payment_tools.stripe.PaymentIntent.retrieve")
@patch("backend.tools.payment_tools.stripe.PaymentIntent.confirm")
def test_payment_confirmation_success(mock_confirm, mock_retrieve):
    """Test successful payment confirmation"""
    mock_retrieve.return_value = MagicMock(status="requires_confirmation")
    mock_confirm.return_value = MagicMock(status="succeeded")
    
    result = payment_tools.confirm_payment("pi_123")
    assert result is True

@patch("backend.tools.payment_tools.stripe.PaymentIntent.retrieve")
def test_payment_already_confirmed(mock_retrieve):
    """Test handling of already confirmed payments"""
    mock_retrieve.return_value = MagicMock(status="succeeded")
    result = payment_tools.confirm_payment("pi_123")
    assert result is True

# --- AR Tools Tests ---
@patch("backend.tools.ar_tools.requests.post")
@patch("backend.tools.ar_tools.upload_to_gcs")
def test_ar_scene_generation_success(mock_upload, mock_post):
    """Test successful AR scene creation"""
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"scene": "3d_data"}
    mock_upload.return_value = "https://storage.googleapis.com/bucket/scene.json"
    
    scene_url = ar_tools.generate_ar_scene(
        location="Grand Canyon",
        landmarks=["Viewpoint 1", "Viewpoint 2"]
    )
    
    assert scene_url.startswith("https://storage.googleapis.com")
    assert "scene.json" in scene_url

@patch("backend.tools.ar_tools.requests.post")
def test_ar_scene_api_failure(mock_post):
    """Test AR API failure handling"""
    mock_post.return_value.status_code = 500
    error = ar_tools.generate_ar_scene("Pyramids", ["Great Pyramid"])
    assert "Error generating AR scene" in error

# --- Comprehensive Tool Validation ---
def test_all_tools_have_tests():
    """Meta-test to ensure all tools are covered"""
    tested_tools = {
        'weather_tool', 'event_tools', 'booking_tools',
        'payment_tools', 'ar_tools'
    }
    assert tested_tools == set(backend.tools.__all__)