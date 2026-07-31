# ==========================================
# process_video.py
# Process a YouTube Video and Create FAISS
# ==========================================

from whisper_utils import get_transcript
from transcript_utils import get_youtube_transcript

from vector_db import (
    split_text,
    create_vector_store,
    save_vector_store
)


# ==========================================
# Process Video
# ==========================================

def process_video(youtube_url):

    print("=" * 60)
    print("Step 1 : Getting Transcript...")
    print("=" * 60)

    transcript = None

    # ------------------------------------------
    # METHOD 1: Try YouTube captions first
    # ------------------------------------------

    try:

        print("Trying YouTube captions/transcript...")

        transcript = get_youtube_transcript(youtube_url)

        if transcript:

            print("YouTube Transcript Retrieved Successfully!")
            print("Using YouTube captions instead of Whisper.\n")

    except Exception as e:

        print(f"YouTube transcript unavailable: {repr(e)}")
        transcript = None


    # ------------------------------------------
    # METHOD 2: Fall back to Whisper
    # ------------------------------------------

    if not transcript:

        print("YouTube transcript not available.")
        print("Falling back to Whisper...\n")

        try:

            transcript = get_transcript(youtube_url)

            print("Whisper Transcript Generated Successfully!\n")

        except Exception as e:

            print(f"Whisper transcription failed: {repr(e)}")

            raise Exception(
                "Could not obtain transcript using either "
                "YouTube captions or Whisper."
            )


    # ------------------------------------------
    # Make sure transcript exists
    # ------------------------------------------

    if not transcript or not transcript.strip():

        raise Exception(
            "Transcript is empty. Unable to process video."
        )


    # ==========================================
    # Step 2 : Split Transcript
    # ==========================================

    print("=" * 60)
    print("Step 2 : Splitting Transcript...")
    print("=" * 60)

    docs = split_text(transcript)

    print(f"Total Chunks Created : {len(docs)}\n")


    # ==========================================
    # Step 3 : Create Vector Database
    # ==========================================

    print("=" * 60)
    print("Step 3 : Creating Vector Database...")
    print("=" * 60)

    vector_store = create_vector_store(docs)

    print("Vector Database Created Successfully!\n")


    # ==========================================
    # Step 4 : Save FAISS
    # ==========================================

    print("=" * 60)
    print("Step 4 : Saving FAISS...")
    print("=" * 60)

    save_vector_store(vector_store)

    print("FAISS Saved Successfully!\n")


    # ==========================================
    # Completed
    # ==========================================

    print("=" * 60)
    print("Video Processing Completed Successfully!")
    print("=" * 60)


# ==========================================
# Main Function
# ==========================================

if __name__ == "__main__":

    youtube_url = input("Enter YouTube URL : ")

    process_video(youtube_url)