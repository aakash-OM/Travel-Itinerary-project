import pytest
from unittest.mock import patch
from backend.tools.payment_tools import create_payment_intent, confirm_payment

@patch("backend.tools.payment_tools.stripe.PaymentIntent.create")
def test_payment_intent_creation(mock_create):
    """Test Stripe payment intent creation"""
    mock_create.return_value = {"id": "pi_123", "client_secret": "secret_123"}
    
    intent = create_payment_intent(10000, "usd", {"trip_id": "TR123"})
    assert intent.id == "pi_123"
    assert intent.client_secret == "secret_123"

@patch("backend.tools.payment_tools.stripe.PaymentIntent.confirm")
def test_payment_confirmation(mock_confirm):
    """Test payment confirmation flow"""
    mock_confirm.return_value = {"status": "succeeded"}
    
    result = confirm_payment("pi_123")
    assert result is True