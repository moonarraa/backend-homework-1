# backend/src/assistant/a2a_assistant.py
from a2a import Assistant
import os

assistant = Assistant("openai", api_key=os.getenv("OPENAI_API_KEY"))

def ask_a2a(prompt: str) -> str:
    return assistant.chat(prompt)