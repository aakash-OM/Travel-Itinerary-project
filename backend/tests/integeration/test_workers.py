from unittest.mock import patch
from backend.workers.booking_worker import process_booking

@patch("backend.workers.booking_worker.payment_tools.confirm_payment")
@patch("backend.workers.booking_worker.booking_tools.book_flight")
def test_booking_workflow(mock_book, mock_confirm):
    """Test async booking workflow"""
    mock_confirm.return_value = True
    mock_book.return_value = {"confirmation": "FL123456"}
    
    result = process_booking({
        "user_id": "test123",
        "payment_intent": "pi_123",
        "flights": [{"id": "FL100"}],
        "email": "test@example.com"
    })
    
    assert "confirmation" in result