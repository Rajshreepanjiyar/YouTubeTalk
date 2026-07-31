import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(youtube_url: str):
    """
    Extract YouTube video ID from normal and shortened URLs.
    """

    patterns = [
        r"(?:youtube\.com/watch\?v=)([\w-]{11})",
        r"(?:youtu\.be/)([\w-]{11})",
        r"(?:youtube\.com/shorts/)([\w-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, youtube_url)

        if match:
            return match.group(1)

    return None


def get_youtube_transcript(youtube_url: str):
    """
    Try to get an existing YouTube transcript/captions.

    Returns transcript text if available.
    Returns None if transcript cannot be obtained.
    """

    video_id = extract_video_id(youtube_url)

    if not video_id:
        return None

    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        text = " ".join(
            snippet.text for snippet in transcript
        )

        return text

    except Exception as e:
        print(f"TRANSCRIPT ERROR: {repr(e)}")
        return None