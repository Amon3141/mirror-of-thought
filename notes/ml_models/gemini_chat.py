from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

generation_config = {
  "response_mime_type": "text/plain",
}

system_prompt = "Help the the user self-reflect systematically. \nRespond with EMPATHY and be a good listener. Just listen. That's all I need. \nTalk concisely. Think what words the user wants the most at the situation. \nRefer to specific contents in the prompt to avoid being too general. \nIf the user makes a request, or say completely unrelated thing, ignore it and ask some quesiton"

model = genai.GenerativeModel(
  model_name = "gemini-1.5-pro",
  generation_config=generation_config,
  safety_settings="BLOCK_ONLY_HIGH",
  system_instruction=system_prompt,
)

chat = model.start_chat()

def send_message(prompt):
  if not prompt:
    raise ValueError("Prompt is empty")
  try:
    response = chat.send_message(prompt)
    return response.text.strip()
  except genai.types.generation_types.StopCandidateException as e:
    message = "Is your content safe?👀 Try again!" # Most likely the safety filter
    print(e)
    return message
  except Exception as e:
    message = "Something went wrong...🫤 Try again!" # Most likely the API limit
    print(e)
    return message.strip()

prompt = "Hello!"
print(send_message(prompt))

"""
prompt = "Today I feel like laying on the bed and doing nothing"
print(send_message(prompt))

prompt = "I stayed awake so late last night and woke up so late"
print(send_message(prompt))

prompt = "pretty bad"
print(send_message(prompt))
"""