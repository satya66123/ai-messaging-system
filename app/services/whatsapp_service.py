from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = "whatsapp:+14155238886"  # Twilio sandbox number
TO_WHATSAPP = "whatsapp:+917893994174"   # your number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(message: str):
    msg = client.messages.create(
        body=message,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )
    return msg.sid