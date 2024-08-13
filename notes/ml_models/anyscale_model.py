# From August 1, 2024, they stopped free plan;;

import os
import openai

ANYSCALE_API_KEY = "aph0_CkcwRQIhAOBL9JWFymGZywvqvwifNKW8gnijaDPVmEqRRXlYbEf2AiAb3qvIcAIIEfKE0ZOnK86pwpQtHTNGqWFjOwJskdxcJRJjEiCkatqDDxhmF9v3YN5kO6Tax0SvY601PQfYAYwlAPoAgBgBIh51c3JfanE1cWR2cjhuaHhocHU1NTU4Z2VjZ2p3N2w6DAihxcmVEhDQk4jpAUIMCPWG6bUGENCTiOkB8gEA"



client = openai.OpenAI(
  api_key = "esecret_ANYSCALE_API_KEY",
  base_url = "https://api.endpoints.anyscale.com/v1"
)

query = "Who won the Australian open 2012 final, and how many sets were played?"

response = client.chat.completions.create(
  model="mistralai/Mistral-7B-Instruct-v0.1",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": query}
  ]
)

print(response.choices[0].message.content)