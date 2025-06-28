import faiss
import numpy as np
import re
from sentence_transformers import SentenceTransformer
from generator import generate_answer


# Clean and normalize context
def clean_context(text):
    text = text.replace("•", " ").replace("▪", " ")
    return re.sub(r"\s+", " ", text).strip()


# Load saved text chunks
with open("faiss_index.txt", "r", encoding="utf-8") as f:
    chunks = f.readlines()

# Load FAISS index
index = faiss.read_index("faiss_index.index")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def ask_question(question, top_k=3, threshold=1.4):
    q_embedding = model.encode([question])
    distances, indices = index.search(np.array(q_embedding), top_k)

    # Apply relevance threshold
    relevant_chunks = [
        chunks[i].strip()
        for i, dist in zip(indices[0], distances[0])
        if dist < threshold
    ]

    # Fallback: use all top_k chunks if nothing passes threshold
    if not relevant_chunks:
        relevant_chunks = [chunks[i].strip() for i in indices[0]]

    context = clean_context("\n".join(relevant_chunks))
    answer = generate_answer(question, context)

    print("\n\033[1;32m✅ Answer:\033[0m\n")
    print(answer)


if __name__ == "__main__":
    print("🤖 AI FAQ Assistant (type 'exit' to quit')")
    while True:
        q = input("\nAsk your question: ")
        if q.lower() == "exit":
            break
        ask_question(q)
