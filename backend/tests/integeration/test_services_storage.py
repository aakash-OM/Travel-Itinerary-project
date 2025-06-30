from unittest.mock import patch
from backend.services.storage_service import upload_to_gcs

@patch("backend.services.storage_service.storage.Client")
def test_gcs_upload(mock_client):
    """Test file upload to Google Cloud"""
    mock_bucket = mock_client.return_value.bucket.return_value
    mock_blob = mock_bucket.blob.return_value
    mock_blob.public_url = "https://storage.example.com/file.txt"
    
    url = upload_to_gcs("test.txt", b"file content")
    assert "https://storage.example.com" in url