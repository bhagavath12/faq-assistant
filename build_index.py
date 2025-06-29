from embed_utils import read_pdf, chunk_text, embed_chunks, save_faiss_index, save_text_chunks

if __name__ == "__main__":
    file_path = "data/sample_faq.pdf"
    text = read_pdf(file_path)
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    save_faiss_index(embeddings)
    save_text_chunks(chunks)
    print(f" Indexed {len(chunks)} chunks from: {file_path}")
