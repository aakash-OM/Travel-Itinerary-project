import celery
from agents.storyteller_agent import StorytellerAgent
from services.storage_service import upload_to_gcs
from utils.logger import logger

app = Celery('story', broker=os.getenv("CELERY_BROKER_URL"))

@app.task
def generate_destination_story(destination: str):
    """Background task for story generation"""
    try:
        storyteller = StorytellerAgent()
        story = storyteller.generate_story(destination)
        
        # Upload components to cloud storage
        for key in ['video', 'ar_scene', 'text']:
            if key in story:
                story[key] = upload_to_gcs(
                    f"stories/{destination}/{key}",
                    story[key]
                )
        
        return story
    except Exception as e:
        logger.error(f"Story generation failed: {str(e)}")
        raise self.retry(exc=e, countdown=120)