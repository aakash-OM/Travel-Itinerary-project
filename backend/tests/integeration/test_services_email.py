from unittest.mock import patch
from backend.services.email_service import send_travel_documents

@patch("backend.services.email_service.SendGridAPIClient.send")
def test_email_delivery(mock_send):
    """Test successful email delivery"""
    mock_send.return_value.status_code = 202
    
    result = send_travel_documents(
        "user@example.com",
        "Your Trip Confirmation",
        "<p>Thank you for booking!</p>",
        [{"path": "ticket.pdf", "name": "ticket.pdf", "type": "application/pdf"}]
    )
    assert result is True