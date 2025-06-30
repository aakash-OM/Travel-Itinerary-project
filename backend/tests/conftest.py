import pytest
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture
def test_client():
    """Provide test client for API tests"""
    return TestClient(app)

@pytest.fixture
def sample_user():
    """Sample user fixture"""
    return {
        "user_id": "test_user_123",
        "email": "test@travelgenius.app",
        "payment_token": "tok_test_valid"
    }