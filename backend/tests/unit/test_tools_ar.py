from unittest.mock import patch
from backend.tools.ar_tools import generate_ar_scene

@patch("backend.tools.ar_tools.requests.post")
def test_ar_generation_success(mock_post):
    """Test AR scene generation"""
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"scene_id": "ar_123"}
    
    scene_url = generate_ar_scene("Tokyo", ["Senso-ji Temple"])
    assert "ar_123" in scene_url

@patch("backend.tools.ar_tools.requests.post")
def test_ar_generation_failure(mock_post):
    """Test AR generation error handling"""
    mock_post.return_value.status_code = 500
    scene_url = generate_ar_scene("Invalid", [])
    assert "Error" in scene_url