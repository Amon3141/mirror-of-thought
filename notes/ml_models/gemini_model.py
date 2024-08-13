import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyADouAB9_Wtr0pB8B0hjnRkl-OqxNsrtQw"
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(prompt):
  model = genai.GenerativeModel("gemini-pro")
  system_prompt = "Help self-reflection by asking content-specific question. Help the user's thought to move forward. Give an accepting comment at first (<= 4 words). Use the similar-level vocabulary as the prompt"
  full_prompt = f"{system_prompt}\n\nUser: {prompt}\nAI:"
  response = model.generate_content(full_prompt)
  return response.text

prompt = "Today I feel like laying on the bed and doing nothing"
#print(get_gemini_response(prompt))