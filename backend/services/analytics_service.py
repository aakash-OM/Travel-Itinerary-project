from google.cloud import bigquery
from datetime import datetime
import os

client = bigquery.Client()

def track_affiliate_click(user_id: str, affiliate: str, destination: str):
    """Logs affiliate link clicks"""
    query = f"""
        INSERT INTO `travel_genius.affiliate_clicks` 
        (user_id, timestamp, affiliate, destination)
        VALUES ('{user_id}', '{datetime.utcnow()}', '{affiliate}', '{destination}')
    """
    client.query(query)

def track_conversion(user_id: str, booking_value: float):
    """Logs successful bookings"""
    query = f"""
        INSERT INTO `travel_genius.conversions` 
        (user_id, timestamp, booking_value, commission)
        VALUES ('{user_id}', '{datetime.utcnow()}', {booking_value}, {booking_value * 0.06})
    """
    client.query(query)