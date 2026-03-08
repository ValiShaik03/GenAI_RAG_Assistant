from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

documents = []

def fit_embeddings(texts):
    global vectorizer, documents
    documents = texts
    vectorizer.fit(texts)

def get_embedding(text):
    return vectorizer.transform([text]).toarray()[0]