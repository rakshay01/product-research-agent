import os
from dotenv import load_dotenv
load_dotenv()

from groq import Groq
from src.tools import search_tool

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_llm(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # The returned message is a ChatCompletionMessage object — use .content
    # instead of subscripting which raises TypeError.
    msg = completion.choices[0].message
    # Support both dict-like and object-like responses for compatibility
    if isinstance(msg, dict):
        return msg.get("content", "")
    return getattr(msg, "content", "")
