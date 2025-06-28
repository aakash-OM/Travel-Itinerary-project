from google.cloud import storage
from utils.config import settings
import os

def upload_to_gcs(file_path: str, data: bytes) -> str:
    """Uploads data to Google Cloud Storage"""
    client = storage.Client()
    bucket = client.bucket(settings.gcs_bucket_name)
    blob = bucket.blob(file_path)
    blob.upload_from_string(data)
    return f"https://storage.googleapis.com/{settings.gcs_bucket_name}/{file_path}"

def generate_signed_url(file_path: str, expiration=3600) -> str:
    """Generates a signed URL for temporary access"""
    client = storage.Client()
    bucket = client.bucket(settings.gcs_bucket_name)
    blob = bucket.blob(file_path)
    return blob.generate_signed_url(
        expiration=expiration,
        method='GET'
    )