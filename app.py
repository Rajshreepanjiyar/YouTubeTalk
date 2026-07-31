# ==========================================
# app.py
# FastAPI Backend
# ==========================================

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


from schemas import (
    VideoRequest,
    ChatRequest,
    ChatResponse
)

from process_video import process_video

from vector_db import (
    load_vector_store,
    get_retriever
)

from url_validator import (
    is_valid_youtube_url,
    video_exists
)


from rag import ask_question


# ==========================================
# Create FastAPI App
# ==========================================

app = FastAPI(
    title="YouTube RAG Chatbot",
    description="Ask questions from any YouTube video using Whisper + FAISS + Groq",
    version="1.0.0"
)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")



# ==========================================
# Global Retriever
# ==========================================

retriever = None


# ==========================================
# Home API
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )

# ==========================================
# Process Video API
# ==========================================

@app.post("/process-video")
def process_video_api(request: VideoRequest):

    global retriever

    # -----------------------------------------
    # Validate URL Format
    # -----------------------------------------

    if not is_valid_youtube_url(request.youtube_url):

        raise HTTPException(
            status_code=400,
            detail="Please enter a valid YouTube URL."
        )

    # -----------------------------------------
    # Check Whether Video Exists
    # -----------------------------------------

    if not video_exists(request.youtube_url):

        raise HTTPException(
            status_code=400,
            detail="This YouTube video does not exist or is not accessible."
        )

    # -----------------------------------------
    # Process Video
    # -----------------------------------------

    process_video(request.youtube_url)

    vector_store = load_vector_store()

    retriever = get_retriever(vector_store)

    return {

        "message": "Video processed successfully."

    }


# ==========================================
# Chat API
# ==========================================

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    global retriever

    if retriever is None:

        raise HTTPException(

            status_code=400,

            detail="Please process a video first."

        )

    answer = ask_question(

        retriever,

        request.question

    )

    return ChatResponse(

        answer=answer

    )