import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=200, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk.strip())
    return chunks


def embed_chunks(chunks):
    return model.encode(chunks, convert_to_numpy=True)

def save_faiss_index(embeddings, output_path="faiss_index"):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, output_path + ".index")
    return index

def save_text_chunks(chunks, path="faiss_index.txt"):
    with open(path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n")
