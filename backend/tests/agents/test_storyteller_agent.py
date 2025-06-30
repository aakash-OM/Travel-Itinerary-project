from unittest.mock import patch
from backend.agents.storyteller_agent import StorytellerAgent

@patch("backend.agents.storyteller_agent.generate_ar_scene")
def test_destination_story(mock_ar):
    """Test story generation with AR"""
    mock_ar.return_value = "https://ar.example.com/swiss_alps"
    
    agent = StorytellerAgent()
    story = agent.generate_story("Switzerland")
    
    assert "swiss_alps" in story["ar_experience"]
    assert "Switzerland" in story["text_summary"]