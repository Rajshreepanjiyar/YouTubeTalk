# =====================================================
# YouTube RAG Chatbot Dockerfile
# =====================================================

# Use official Python image
FROM python:3.12-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Print logs immediately
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# -----------------------------------------------------
# Install system dependencies
# -----------------------------------------------------

RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------
# Copy requirements first
# (Better Docker caching)
# -----------------------------------------------------

COPY requirements.txt .

# Upgrade pip

RUN pip install --upgrade pip

# Install Python dependencies

RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------
# Copy complete project
# -----------------------------------------------------

COPY . .

# -----------------------------------------------------
# Create required folders
# -----------------------------------------------------

RUN mkdir -p data/audio

RUN mkdir -p data/transcript

RUN mkdir -p data/faiss

# -----------------------------------------------------
# Expose FastAPI Port
# -----------------------------------------------------

EXPOSE 8000

# -----------------------------------------------------
# Run FastAPI
# -----------------------------------------------------

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]