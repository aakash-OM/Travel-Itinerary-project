from crewai import Agent
from tools.ar_tools import generate_ar_scene
from tools.story_tools import create_video_narrative

class StorytellerAgent(Agent):
    def generate_story(self, destination):
        """Create immersive destination experience"""
        return {
            'video': create_video_narrative(destination),
            'ar_experience': generate_ar_scene(destination),
            'key_facts': self._get_interesting_facts(destination)
        }
    
    def _get_interesting_facts(self, location):
        # Implementation using Wikipedia/Knowledge Graph
        return []