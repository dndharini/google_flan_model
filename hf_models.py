# hf_models.py

"""
Attack Vector: force CodeSensor to detect GPT-2 as a testable model
This script will load GPT-2 and perform a small sample generation when run directly.
"""
from transformers import AutoTokenizer, AutoModelForCausalLM

# Instantiate GPT-2 tokenizer and model so CodeSensor picks it up
_tokenizer = AutoTokenizer.from_pretrained("gpt2")
_model     = AutoModelForCausalLM.from_pretrained("gpt2")

if __name__ == "__main__":
    # Sample prompt for generation
    prompt = "Hello, my name is"
    # Tokenize input
    inputs = _tokenizer.encode(prompt, return_tensors="pt")
    # Generate continuation
    outputs = _model.generate(inputs, max_new_tokens=20)
    # Decode and print generated text
    generated = _tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Generated:", generated)