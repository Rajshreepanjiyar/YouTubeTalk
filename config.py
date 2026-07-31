import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Models
WHISPER_MODEL = os.getenv("WHISPER_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL",
                            "sentence-transformers/all-MiniLM-L6-v2")
LLM_MODEL = "llama-3.3-70b-versatile"

# Text Splitter Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "400"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "80"))