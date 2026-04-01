from fastapi import APIRouter
from app.services.gmail_service import read_latest_email
from app.services.ollama_service import generate_response
from app.utils.rules import should_reply

router = APIRouter()


@router.get("/smart-automation")
def smart_automation():
    email = read_latest_email()

    should_send, reason = should_reply(email)

    if not should_send:
        return {
            "email": email,
            "status": "skipped",
            "reason": reason
        }

    ai_message = generate_response(
        email,
        "whatsapp",
        "friendly"
    )

    return {
        "email": email,
        "ai_message": ai_message,
        "status": "generated_only",
        "reason": reason
    }