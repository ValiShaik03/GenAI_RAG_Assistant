import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embeddings import get_embedding, fit_embeddings
from groq import Groq


# -----------------------------
# GROQ API KEY
# -----------------------------
client = Groq(api_key="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")


# -----------------------------
# LOAD DOCUMENTS
# -----------------------------
with open("docs.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

chunks = []

for doc in docs:
    chunks.append(doc["content"])


# -----------------------------
# TRAIN EMBEDDINGS
# -----------------------------
fit_embeddings(chunks)


# CREATE DOCUMENT EMBEDDINGS
embeddings = []

for text in chunks:
    embeddings.append(get_embedding(text))

embeddings = np.array(embeddings)


# -----------------------------
# SIMILARITY SEARCH
# -----------------------------
def search(query):

    query_embedding = get_embedding(query)

    similarities = cosine_similarity(
        [query_embedding], embeddings
    )[0]

    # Get top 3 relevant chunks
    top_indices = similarities.argsort()[-3:][::-1]

    results = []

    for i in top_indices:
        results.append(chunks[i])

    return results


# -----------------------------
# GENERATE ANSWER (RAG)
# -----------------------------
def generate_answer(question):

    context_chunks = search(question)

    context = "\n".join(context_chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the question ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context say:
"I don't have enough information."
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content