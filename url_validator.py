import re
from yt_dlp import YoutubeDL


def is_valid_youtube_url(url: str) -> bool:
    """
    Checks whether the URL has a valid YouTube format.
    """

    pattern = re.compile(
        r"^(https?://)?(www\.)?"
        r"(youtube\.com/watch\?v=|youtu\.be/)"
        r"[\w\-]{11}.*$"
    )

    return bool(pattern.match(url))


def video_exists(url: str) -> bool:
    """
    Checks whether the YouTube video actually exists.
    """

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)

        return True

    except Exception:
        return False