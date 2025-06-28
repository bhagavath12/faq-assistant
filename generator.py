from llama_cpp import Llama

# Initialize model (adjust path to your GGUF file)
llm = Llama(
    model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6,  # set based on your CPU
    n_batch=512,
    verbose=False
)

def generate_answer(question, context):
    prompt = f"""[INST] Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion:\n{question} [/INST]"""
    
    output = llm(prompt, max_tokens=512, stop=["</s>"])
    return output["choices"][0]["text"].strip()
