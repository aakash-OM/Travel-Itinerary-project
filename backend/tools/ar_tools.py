import requests
import json
from utils.config import settings
from utils.storage_service import upload_to_gcs

def generate_ar_scene(location: str, landmarks: list) -> str:
    """Generates an AR experience for a location"""
    try:
        response = requests.post(
            "https://api.echo3d.com/v1/ar/generate",
            headers={"Authorization": f"Bearer {settings.echo3d_key}"},
            json={
                "location": location,
                "landmarks": landmarks,
                "quality": "high"
            }
        )
        response.raise_for_status()
        scene_data = response.json()
        
        # Upload to cloud storage
        scene_url = upload_to_gcs(
            f"ar-scenes/{location}.json",
            json.dumps(scene_data).encode()
        )
        return scene_url
    except Exception as e:
        return f"Error generating AR scene: {str(e)}"