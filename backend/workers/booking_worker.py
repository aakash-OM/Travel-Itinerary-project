import time
from celery import Celery
from services import email_service
from tools import booking_tools, payment_tools
from models.booking import BookingConfirmation
from utils.logger import logger

app = Celery('booking', broker=os.getenv("CELERY_BROKER_URL"))

@app.task
def process_booking(booking_data: dict):
    """Background task for booking processing"""
    try:
        # Step 1: Confirm payment
        if not payment_tools.confirm_payment(booking_data['payment_intent']):
            raise ValueError("Payment failed")
        
        # Step 2: Book flights
        flights = []
        for flight in booking_data['flights']:
            result = booking_tools.book_flight(flight)
            flights.append(result)
        
        # Step 3: Book hotel
        hotel = booking_tools.book_hotel(booking_data['hotel'])
        
        # Step 4: Generate documents
        confirmation = BookingConfirmation(
            booking_id=f"BK-{time.time()}",
            user_id=booking_data['user_id'],
            flights=flights,
            hotels=[hotel],
            total_cost=booking_data['total']
        )
        
        # Step 5: Email documents
        email_service.send_travel_documents(
            email=booking_data['email'],
            subject="Your Travel Confirmation",
            content="Your trip details are attached",
            attachments=[generate_confirmation_pdf(confirmation)]
        )
        
        return confirmation.dict()
    except Exception as e:
        logger.error(f"Booking failed: {str(e)}")
        raise self.retry(exc=e, countdown=60)