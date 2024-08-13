# Hugging Face's transformers is not good enough

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")

def generate(instruction, knowledge, dialog):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(
      input_ids, 
      max_length=100, 
      min_length=8, 
      top_p=0.85,
      temperature=0.8,
      do_sample=True,
      no_repeat_ngram_size=3,
      repetition_penalty=1.5,
    )
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output
  
# Instruction for a chitchat task
instruction = "Instruction: Ask a question to encourage self reflection"
# knowldge
knowledge = ""

dialog = [
  "I think I am being hated by everybody",
  "Are you afraid of being hated by everybody?",
  "I think so. I think everyone does"
]
response = generate(instruction, knowledge, dialog)
print(response)

def return_response(text):
  dialog = [text]
  return generate(instruction, knowledge, dialog)