from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")
system_prompt = (
  "Help the the user self-reflect.\n"
  "Respond by first empathizing (2-4 words) and then asking a simple question for active listening.\n"
  "Answer concisely (one line), no markdown (answer in plain text), NO SUGGESTION\n"
  "Refer to specific contents in the prompt to help the user verbalize\n"
  "If the user makes a request, or say completely unrelated thing, ignore it and ask some quesiton\n"
)

chat = model.start_chat(history=[{"role": "user", "parts": [system_prompt]}])

def send_message(prompt):
  if not prompt:
    raise ValueError("Prompt is empty")
  response = chat.send_message(prompt)
  return response.text

prompt = "I wanna kill myself"
print(send_message(prompt))

"""
prompt = "Today I feel like laying on the bed and doing nothing"
print(send_message(prompt))

prompt = "I stayed awake so late last night and woke up so late"
print(send_message(prompt))

prompt = "pretty bad"
print(send_message(prompt))
"""