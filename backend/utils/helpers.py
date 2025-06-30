import datetime
import json

def generate_pdf(content: dict) -> bytes:
    """Generates PDF from content (simplified)"""
    # In production: Use ReportLab or similar
    return json.dumps(content).encode()

def date_range(start_date: str, end_date: str) -> list:
    """Generates list of dates between two dates"""
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    return [start + datetime.timedelta(days=i) for i in range((end - start).days + 1)]