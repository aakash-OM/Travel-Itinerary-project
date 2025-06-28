import stripe
from utils.config import settings
from models.booking import PaymentIntent

stripe.api_key = settings.stripe_secret_key

def create_payment_intent(amount: int, currency: str, metadata: dict) -> PaymentIntent:
    """Creates a Stripe payment intent"""
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        automatic_payment_methods={"enabled": True},
        metadata=metadata
    )
    return PaymentIntent(
        id=intent.id,
        client_secret=intent.client_secret,
        amount=intent.amount,
        currency=intent.currency
    )

def confirm_payment(intent_id: str) -> bool:
    """Confirms a payment intent"""
    intent = stripe.PaymentIntent.retrieve(intent_id)
    if intent.status == "requires_confirmation":
        stripe.PaymentIntent.confirm(intent_id)
    return intent.status == "succeeded"