from twilio.rest import Client

ACCOUNT_SID = "AC7cbb5f575c1190b8af31dc0bbbe83d1a"
AUTH_TOKEN = "0166267e067b1bebca2c0da80d368eaf"

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