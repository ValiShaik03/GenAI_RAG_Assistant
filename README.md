# 🧠 Production-Grade GenAI RAG Assistant

A **Retrieval-Augmented Generation (RAG) based AI assistant** that answers user questions using information retrieved from a document knowledge base.

The system converts documents into embeddings, performs similarity search, retrieves relevant context, and generates grounded responses using a Large Language Model.

---

# 🚀 Features

* Document-based Question Answering
* Embedding-based similarity search
* Retrieval-Augmented Generation (RAG)
* Chat interface for user interaction
* Context-grounded answers
* Safe fallback response when information is unavailable
* Fast LLM inference using Groq API

---

# 🛠 Tech Stack

Backend:

* Python
* Flask

Frontend:

* HTML
* JavaScript

AI Components:

* Groq API (Llama-3.1 Model)
* Embeddings using TF-IDF
* Cosine Similarity Search

Libraries:

* Flask
* Groq
* NumPy
* Scikit-Learn

---

# 📂 Project Structure

```
rag_assistant/
│
├── app.py
├── rag.py
├── embeddings.py
├── docs.json
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── script.js
│
└── README.md
```

---

# ⚙️ How the System Works

```
User Query
     ↓
Query Embedding
     ↓
Similarity Search (Vector Retrieval)
     ↓
Top Relevant Document Chunks
     ↓
Prompt Construction
     ↓
LLM Response Generation
     ↓
Final Answer to User
```

This approach ensures the model answers **based on documents instead of generating unsupported information**.

---

# 📚 Document Knowledge Base

Documents are stored in **docs.json**.

Example:

```
{
  "title": "Reset Password",
  "content": "Users can reset their password by going to Settings and selecting Security."
}
```

These documents are converted into embeddings and stored for similarity search.

---

# 🔎 Retrieval Process

1. Convert user query into embedding
2. Compute cosine similarity with document embeddings
3. Retrieve top relevant document chunks
4. Inject retrieved context into the LLM prompt
5. Generate grounded answer

---

# 🧪 Example Queries

```
How can I reset my password?
How do I change my email?
How can I enable two factor authentication?
How can I contact support?
```

Example response:

```
Users can reset their password by going to Settings and selecting Security.
```

If information is not available:

```
I don't have enough information.
```

---

# 📦 Installation

Clone the repository:

```
git clone https://github.com/your-username/genai-rag-assistant.git
cd genai-rag-assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🔑 Setup Groq API Key

Get your API key from:

https://console.groq.com/keys

Add your key in **rag.py**:

```
client = Groq(api_key="YOUR_GROQ_API_KEY")
```

---

# ▶️ Run the Application

Start the Flask server:

```
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

# 📊 Evaluation Criteria Covered

✔ Document Knowledge Base
✔ Embedding Generation
✔ Similarity Search
✔ Retrieval-Augmented Generation
✔ LLM Integration
✔ Chat Interface
✔ Safe Fallback Responses

---

# 🎥 Demo

The demo video explains:

* Project architecture
* RAG workflow
* Code walkthrough
* Application demo

---

# 📌 Future Improvements

* Persistent vector database (FAISS / Chroma)
* Conversation memory
* Document chunking (300–500 tokens)
* Better UI
* Authentication & user sessions

---

# 👨‍💻 Author

Shaik Mahaboob Vali
AI / Machine Learning Enthusiast
