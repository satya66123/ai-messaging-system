from fastapi import FastAPI
from app.services.ollama_service import generate_response
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str
    type: str  # whatsapp / email
    tone: str = "professional"  # optional

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Messaging System Running"}

@app.post("/ask")
def ask_ai(request: PromptRequest):
    response = generate_response(
        request.prompt,
        request.type,
        request.tone
    )
    return {"response": response}