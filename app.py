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

from url_validator import is_valid_youtube_url


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
    # Validate YouTube URL Format
    # -----------------------------------------

    if not is_valid_youtube_url(request.youtube_url):
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid YouTube URL."
        )

    # -----------------------------------------
    # Process Video
    # -----------------------------------------

    try:
        # Download audio + Whisper transcription
        # + create FAISS vector database
        process_video(request.youtube_url)

        # Load vector database
        vector_store = load_vector_store()

        # Create retriever
        retriever = get_retriever(vector_store)

        return {
            "message": "Video processed successfully."
        }

    except Exception as e:

        # Print actual error in Render logs
        print(f"VIDEO PROCESSING ERROR: {repr(e)}")

        raise HTTPException(
            status_code=500,
            detail="Failed to process the YouTube video."
        )

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