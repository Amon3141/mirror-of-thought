# They make me pay $5, and I couldn't register my credit card

import os
from openai import OpenAI

# Set up the API key
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

def get_response(prompt):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
  )
  return response.choices.message.content

# Use the function
user_prompt = "What is the capital of France?"
response = get_response(user_prompt)
print(response)