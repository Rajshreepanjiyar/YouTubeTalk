# ==========================================
# vector_db.py
# ==========================================

import os

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS


# ==========================================
# Split Transcript
# ==========================================

def split_text(transcript):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )

    docs = splitter.create_documents([transcript])

    return docs


# ==========================================
# Embedding Model
# ==========================================

def get_embedding_model():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


# ==========================================
# Create Vector Store
# ==========================================

def create_vector_store(docs):

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        docs,
        embeddings
    )

    return vector_store


# ==========================================
# Save FAISS
# ==========================================

def save_vector_store(vector_store):

    os.makedirs("data/faiss", exist_ok=True)

    vector_store.save_local("data/faiss")

    print("FAISS saved successfully.")


# ==========================================
# Load FAISS
# ==========================================

def load_vector_store():

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        "data/faiss",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


# ==========================================
# Retriever
# ==========================================

def get_retriever(vector_store):

    retriever = vector_store.as_retriever(

        search_type="similarity",

        search_kwargs={
            "k":10
        }

    )

    return retriever