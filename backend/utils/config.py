import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    weather_api_key: str = os.getenv("WEATHERAPI_KEY")
    stripe_secret_key: str = os.getenv("STRIPE_SECRET_KEY")
    sendgrid_key: str = os.getenv("SENDGRID_API_KEY")
    gcs_bucket_name: str = os.getenv("GCS_BUCKET", "travel-genius-assets")
    
    class Config:
        env_file = ".env"

settings = Settings()