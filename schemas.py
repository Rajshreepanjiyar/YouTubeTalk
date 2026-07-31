# ==========================================
# schemas.py
# Request Models for FastAPI
# ==========================================

from pydantic import BaseModel


# ==========================================
# Process Video Request
# ==========================================

class VideoRequest(BaseModel):

    youtube_url: str


# ==========================================
# Chat Request
# ==========================================

class ChatRequest(BaseModel):

    question: str


# ==========================================
# Chat Response
# ==========================================

class ChatResponse(BaseModel):

    answer: str