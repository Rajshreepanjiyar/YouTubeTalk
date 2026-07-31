# ==========================================
# whisper_utils.py
# Download YouTube Audio
# Convert Speech to Text using Whisper
# ==========================================

import os
import yt_dlp
import whisper
import torch

from config import WHISPER_MODEL


# ==========================================
# Delete old audio file
# ==========================================

def clean_old_audio():

    audio_folder = "data/audio"

    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    for file in os.listdir(audio_folder):

        file_path = os.path.join(audio_folder, file)

        if os.path.isfile(file_path):
            os.remove(file_path)


# ==========================================
# Download YouTube Audio
# ==========================================

def download_audio(youtube_url):

    clean_old_audio()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "data/audio/audio.%(ext)s",
        "quiet": False,
        "noplaylist": True,
    }

    try:
        print(f"Attempting to download: {youtube_url}")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

    except Exception as e:
        print(f"YT-DLP ERROR: {repr(e)}")
        raise

    for file in os.listdir("data/audio"):
        if file.startswith("audio"):
            return os.path.join("data/audio", file)

    raise Exception("Audio download failed.")
# ==========================================
# Speech to Text using Whisper
# ==========================================

def transcribe_audio(audio_path):

    device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"Using Device : {device}")

    model = whisper.load_model(WHISPER_MODEL).to(device)

    result = model.transcribe(audio_path)

    transcript = result["text"]

    return transcript


# ==========================================
# Complete Pipeline
# ==========================================

def get_transcript(youtube_url):

    audio_path = download_audio(youtube_url)

    transcript = transcribe_audio(audio_path)

    return transcript