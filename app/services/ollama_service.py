import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt: str, msg_type: str, tone: str):
    system_prompt = f"""
    You are an AI assistant that helps summarize and respond to emails.

    STRICT RULES:
    - Do NOT assume responsibility for actions in the email
    - Do NOT say "we accessed" or "we did"
    - Respond as a neutral assistant
    - Keep response helpful and safe

    STYLE:
    - WhatsApp → short, friendly
    - Email → professional

    User email:
    {prompt}
    """

    payload = {
        "model": "llama3",
        "prompt": system_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Error from Ollama"
