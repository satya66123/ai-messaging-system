from pydantic import BaseModel
from app.services.gmail_service import read_latest_email
from app.services.ollama_service import generate_response
from app.services.whatsapp_service import send_whatsapp_message
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from app.routes.automation_routes import router as automation_router




templates = Jinja2Templates(directory="templates")


class PromptRequest(BaseModel):
    prompt: str
    type: str  # whatsapp / email
    tone: str = "professional"  # optional

app = FastAPI()

app.include_router(automation_router)

#@app.get("/")
#def home():
    #return {"message": "AI Messaging System Running"}

@app.post("/ask")
def ask_ai(request: PromptRequest):
    response = generate_response(
        request.prompt,
        request.type,
        request.tone
    )
    return {"response": response}

@app.get("/read-email")
def read_email():
    email = read_latest_email()
    return {"email": email}

@app.get("/ai-whatsapp")
def ai_whatsapp():
    prompt = "Client asking for project update"

    ai_message = generate_response(
        prompt,
        "whatsapp",
        "friendly"
    )

    sid = send_whatsapp_message(ai_message)

    return {
        "ai_message": ai_message,
        "status": "sent",
        "sid": sid

    }



@app.get("/full-automation")
def full_automation():
    # Step 1: Read email
    email = read_latest_email()

    # Step 2: Generate AI reply
    ai_message = generate_response(
        email,
        "whatsapp",
        "friendly"
    )

    # Step 3: Send to WhatsApp
    sid = send_whatsapp_message(ai_message)

    return {
        "email": email,
        "ai_message": ai_message,
        "status": "sent",
        "sid": sid
    }

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/auto-reply")
def auto_reply():
    email = read_latest_email()

    reply = generate_response(
        email,
        "email",
        "professional"
    )

    return {
        "email": email,
        "reply": reply
    }
@app.get("/send-whatsapp")
def send_whatsapp():
    sid = send_whatsapp_message("Hello from AI system 🚀")
    return {"status": "sent", "sid": sid}
