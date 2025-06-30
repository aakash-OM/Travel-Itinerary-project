from backend.agents.pricing_agent import PricingAgent

def test_price_prediction():
    """Test price prediction logic"""
    agent = PricingAgent()
    prediction = agent.predict_prices(
        route="NYC-LON",
        travel_date="2024-12-20"
    )
    
    assert prediction["best_booking_day"] > 0
    assert prediction["predicted_low"] < prediction["predicted_high"]