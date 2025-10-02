import os
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

load_dotenv()


client = Cerebras(
    # This is the default and can be omitted
    api_key=os.getenv("CERERAS_API_KEY")
)

stream = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "why is fast inference important for an LLM agent in 2025?"
        }
    ],
    model="llama-4-scout-17b-16e-instruct",
    stream=True,
    max_completion_tokens=20000,
    temperature=0.7,
    top_p=0.8
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")