from crewai import Agent
from tools.booking_tools import flight_booker, hotel_booker
from services.payment import process_payment
from services.email_service import send_tickets

class BookerAgent(Agent):
    def book_flight(self, user, itinerary):
        """Autonomous flight booking"""
        flight = flight_booker.find_best(
            origin=user.location,
            destination=itinerary.destination,
            dates=itinerary.dates
        )
        
        # Process payment
        payment = process_payment(user.payment_token, flight.price)
        
        # Book ticket
        ticket = flight_booker.confirm_booking(
            flight.id,
            user_details=user.info,
            payment_id=payment.id
        )
        
        # Deliver tickets
        send_tickets(user.email, ticket)
        return ticket