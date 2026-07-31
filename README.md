# YouTube RAG Chatbot

## Overview

YouTube RAG Chatbot is an AI-powered application that allows users to ask questions about any public YouTube video.

The application automatically downloads the video audio, converts speech into text using OpenAI Whisper, creates semantic embeddings using Sentence Transformers, stores them in a FAISS vector database, and generates accurate answers using Retrieval-Augmented Generation (RAG) with Groq Llama 3.3.

---

# Features

- Process any public YouTube video
- Automatic Speech-to-Text using OpenAI Whisper
- Transcript generation
- Intelligent text chunking
- Semantic embeddings using Sentence Transformers
- FAISS vector database
- Retrieval-Augmented Generation (RAG)
- Groq Llama 3.3 Large Language Model
- FastAPI backend
- HTML, CSS and JavaScript frontend
- Environment variable support using `.env`
- Docker-ready project for deployment

---

# Project Architecture

```text
                User
                  │
                  ▼
        HTML / CSS / JavaScript
                  │
                  ▼
              FastAPI Backend
                  │
                  ▼
        YouTube Video URL
                  │
                  ▼
               yt-dlp
                  │
                  ▼
              FFmpeg Audio
                  │
                  ▼
          OpenAI Whisper
                  │
                  ▼
             Transcript
                  │
                  ▼
      Recursive Text Splitter
                  │
                  ▼
    Sentence Transformers Embeddings
                  │
                  ▼
             FAISS Vector Database
                  │
                  ▼
           Relevant Chunks
                  │
                  ▼
           Groq Llama 3.3
                  │
                  ▼
             Final Answer
```

---

# Project Structure

```text
YouTube_Chatbot_Final/

│── app.py
│── config.py
│── process_video.py
│── whisper_utils.py
│── vector_db.py
│── rag.py
│── schemas.py
│── url_validator.py

│── requirements.txt
│── README.md
│── Dockerfile
│── docker-compose.yml
│── .dockerignore
│── .env

│── templates/
│      └── index.html

│── static/
│      ├── style.css
│      └── script.js

│── data/
│      ├── audio/
│      ├── transcript/
│      └── faiss/

│── tests/

│── venv/
```

---

# Technology Stack

## Backend

- Python
- FastAPI

## Frontend

- HTML
- CSS
- JavaScript

## Artificial Intelligence

- OpenAI Whisper
- LangChain
- Sentence Transformers
- Groq Llama 3.3

## Vector Database

- FAISS

## Audio Processing

- yt-dlp
- FFmpeg

## Deployment

- Docker
- Docker Hub
- AWS EC2 (Planned)
- Render (Planned)

---

# Installation

## Clone the Repository

```bash
git clone <your-github-repository-url>

cd YouTube_Chatbot_Final
```

## Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

WHISPER_MODEL=base

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

CHUNK_SIZE=1000

CHUNK_OVERLAP=200
```

---

# Running the Project

Start the FastAPI server.

```bash
uvicorn app:app --reload
```

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

---

# Application Workflow

1. User enters a YouTube video URL.
2. The application downloads the audio using yt-dlp.
3. OpenAI Whisper converts the audio into text.
4. The transcript is divided into smaller chunks.
5. Sentence Transformers generate vector embeddings.
6. Embeddings are stored in the FAISS vector database.
7. The user asks a question.
8. Relevant transcript chunks are retrieved.
9. Groq Llama 3.3 generates the final answer.

---

# Screenshots

The following screenshots will be added after deployment.

- Home Page
- Video Processing
- Chat Interface
- AI Response

---

# Future Improvements

- Multi-language support
- Multiple video indexing
- Chat history
- Timestamp-based answers
- Source citations
- User authentication
- Cloud deployment
- CI/CD pipeline

---

# Author

Raj Shree

Bachelor of Technology (Computer Science and Engineering)

Silicon University

Areas of Interest:

- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Generative AI
- Cloud Computing

---

# License

This project is intended for educational and learning purposes.