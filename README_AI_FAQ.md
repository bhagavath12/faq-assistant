# 🧠 Offline AI FAQ Assistant

A lightweight, fully offline AI-powered FAQ assistant that uses semantic search (FAISS + sentence-transformers) and a local large language model (Mistral 7B GGUF) to generate contextual answers from PDFs.

---

## 💡 Features

- 🔍 Semantic search using `sentence-transformers` + FAISS
- 📄 Indexes content from your custom PDFs
- 🤖 Local answer generation using `llama-cpp-python` and **Mistral 7B Instruct** (GGUF)
- 💾 Completely offline — no internet or OpenAI API required
- 🧠 Designed for university FAQs, onboarding handbooks, or research papers

---

## 🛠 Tech Stack

- `sentence-transformers` for text embeddings
- `FAISS` for similarity search
- `PyMuPDF` for PDF parsing
- `llama-cpp-python` to run local LLM (`mistral-7b-instruct-v0.1.Q4_K_M.gguf`)

---

## 🚀 How to Use

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Put your PDF inside** `data/` (e.g. `data/sample_faq.pdf`)

3. **Build the FAISS index**

```bash
python build_index.py
```

4. **Run the assistant**

```bash
python app.py
```

Ask questions like:

```txt
What GPA is required for co-op?
When does registration open?
```

---

## 🧠 Model Info

This uses the [`mistral-7b-instruct-v0.1.Q4_K_M.gguf`](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) model. Put the `.gguf` file inside the `models/` folder.

> Make sure the model filename in `generator.py` matches exactly.

---

## 📁 Project Structure

```
faq/
├── app.py                  ← CLI app
├── build_index.py          ← PDF → chunks → FAISS index
├── clean_utils.py          ← Preprocessing helpers
├── embed_utils.py          ← PDF parsing + embedding
├── generator.py            ← Local LLM inference
├── data/                   ← Your PDF files
├── faiss_index.*           ← Saved vector index
├── models/                 ← GGUF model goes here
├── .gitignore
└── README.md
```

---

## 👤 Author

**Bakaram Pranadir Bhagavath Sena Reddy**  
B.E. CSE (AI) — Sathyabama University

---

## 🪪 License

MIT License