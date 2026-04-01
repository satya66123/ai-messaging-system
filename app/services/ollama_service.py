import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt: str, msg_type: str, tone: str):
    system_prompt = f"""
    You are an AI messaging assistant.

    STRICT RULES:
    - Only return the final message
    - No explanations or notes
    - Do NOT use placeholders like [Name], [Role], [Your Name]
    - Avoid overused phrases like "I hope this email finds you well"
    - Keep it natural and realistic

    STYLE:
    - WhatsApp → short, friendly (2-3 lines)
    - Email → professional, concise (5-6 lines max)

    If details are missing, keep it simple and generic but natural.

    Tone: {tone}
    Type: {msg_type}

    User request: {prompt}
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
