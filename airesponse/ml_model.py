from transformers import pipeline, Conversation

# Load a pre-trained model and tokenizer
generator = pipeline(
  'conversational', 
  model='microsoft/DialoGPT-medium',
  device=0
)

# Function to generate a response
def generate_response(input_text):
  response = generator(
    input_text, 
    max_length=30, 
    num_return_sequences=1, 
    truncation=True,
    clean_up_tokenization_spaces=True
  )
  return response[0]['generated_text']

def generate_response_conv(input_text):
  conversation = Conversation(input_text)
  response = generator(conversation)
  return response

print(generate_response_conv("I'm a student"))