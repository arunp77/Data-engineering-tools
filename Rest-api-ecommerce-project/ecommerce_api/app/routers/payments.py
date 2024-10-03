# app/routers/payments.py
import stripe
from fastapi import APIRouter, HTTPException
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

router = APIRouter()

@router.post("/create-payment-intent")
def create_payment_intent(amount: float):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # amount in cents
            currency='usd',
        )
        return {"client_secret": intent.client_secret}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))
