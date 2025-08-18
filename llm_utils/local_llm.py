# llm_utils/local_llm.py
from llama_cpp import Llama
import os

# Path to your local GGUF model file
MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# Load model once (can take time)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,       # context size
    n_threads=8,      # adjust based on CPU
    verbose=False
)

def get_llm_response(prompt):
    response = llm(prompt, max_tokens=500, stop=["</s>"])
    return response["choices"][0]["text"].strip()
