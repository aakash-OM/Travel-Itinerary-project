from backend.utils.helpers import date_range, generate_pdf

def test_date_range_generation():
    """Test date sequence generation"""
    dates = date_range("2024-07-01", "2024-07-03")
    assert len(dates) == 3
    assert dates[1].strftime("%Y-%m-%d") == "2024-07-02"

def test_pdf_generation():
    """Test PDF document creation"""
    content = {"confirmation": "ABC123"}
    pdf = generate_pdf(content)
    assert b"ABC123" in pdf