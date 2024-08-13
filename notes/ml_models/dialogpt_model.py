# Hugging Face's transformers is not good enough

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
  
def generate_response(prompt, top_k=None, top_p=None):
  input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
  
  # Print debugging information
  print(f"Using top_k: {top_k}, top_p: {top_p}")
  
  attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
  
  chat_history_ids = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=100,  # Adjust as needed
    pad_token_id=tokenizer.eos_token_id,
    top_k=top_k,
    top_p=top_p,
    do_sample=True, 
    no_repeat_ngram_size=2,
  )
  
  response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
  print("DialoGPT: {}".format(response))
  return response


prompt = "I'm going to university from next year, but I'm nervous if I can make friends there"
print(generate_response(prompt, top_k=60))
  