"""Download a YouTube video at the highest available quality."""

import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

import yt_dlp

YOUTUBE_HOSTS = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtu.be",
}
DOWNLOADS = Path("downloads")


def is_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and parsed.hostname in YOUTUBE_HOSTS


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python app.py "https://www.youtube.com/watch?v=VIDEO_ID"')
        return 1

    url = sys.argv[1].strip()
    if not is_youtube_url(url):
        print("Error: enter a valid YouTube video URL.")
        return 1
    if not shutil.which("ffmpeg"):
        print("Error: FFmpeg is required to merge the highest-quality video and audio streams.")
        print("Install it on macOS with: brew install ffmpeg")
        return 1

    DOWNLOADS.mkdir(exist_ok=True)
    options = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": str(DOWNLOADS / "%(title).150B [%(id)s].%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        "no_warnings": False,
    }

    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            info = downloader.extract_info(url, download=True)
    except yt_dlp.utils.DownloadError as error:
        print(f"Download failed: {error}")
        return 1

    print(f"\nFinished: {info.get('title', 'video')}")
    print(f"Saved in: {DOWNLOADS.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
