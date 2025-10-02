from cerebras.cloud.sdk import Cerebras
import os
from dotenv import load_dotenv

load_dotenv()

client = Cerebras(api_key=os.getenv("CERERAS_API_KEY"))

def ask_ai(prompt: str):
    """Get AI response from Cerebras"""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-4-scout-17b-16e-instruct",
        max_tokens=600,
        temperature=0.2
    )
    return chat_completion.choices[0].message.content
