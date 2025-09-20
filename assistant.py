import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    raise Exception("Please set your PERPLEXITY_API_KEY in your environment.")

def ask_perplexity(user_input):
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post("https://api.perplexity.ai/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        assistant_msg = response.json()["choices"][0]["message"]["content"]
        return assistant_msg
    except requests.exceptions.RequestException as e:
        error_message = f"API request failed: {e}"
        return error_message