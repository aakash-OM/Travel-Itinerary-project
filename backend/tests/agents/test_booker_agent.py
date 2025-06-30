from unittest.mock import patch
from backend.agents.booker_agent import BookerAgent

@patch("backend.agents.booker_agent.booking_tools.book_hotel")
@patch("backend.agents.booker_agent.payment_tools.process_payment")
def test_hotel_booking(mock_pay, mock_book):
    """Test hotel booking workflow"""
    mock_pay.return_value = "pay_123"
    mock_book.return_value = {"confirmation": "HTL456"}
    
    agent = BookerAgent()
    booking = agent.book_hotel(
        user=MagicMock(),
        hotel_details={"name": "Luxury Resort", "nights": 3}
    )
    
    assert booking["confirmation"] == "HTL456"