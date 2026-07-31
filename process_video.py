# ==========================================
# process_video.py
# Process a YouTube Video and Create FAISS
# ==========================================

from whisper_utils import get_transcript

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
    print("Step 1 : Generating Transcript...")
    print("=" * 60)

    transcript = get_transcript(youtube_url)

    print("Transcript Generated Successfully!\n")


    print("=" * 60)
    print("Step 2 : Splitting Transcript...")
    print("=" * 60)

    docs = split_text(transcript)

    print(f"Total Chunks Created : {len(docs)}\n")


    print("=" * 60)
    print("Step 3 : Creating Vector Database...")
    print("=" * 60)

    vector_store = create_vector_store(docs)

    print("Vector Database Created Successfully!\n")


    print("=" * 60)
    print("Step 4 : Saving FAISS...")
    print("=" * 60)

    save_vector_store(vector_store)

    print("FAISS Saved Successfully!\n")


    print("=" * 60)
    print("Video Processing Completed Successfully!")
    print("=" * 60)


# ==========================================
# Main Function
# ==========================================

if __name__ == "__main__":

    youtube_url = input("Enter YouTube URL : ")

    process_video(youtube_url)