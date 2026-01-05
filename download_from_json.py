import os
import json
import sys
import yt_dlp


DOWNLOADS_DIR = "downloads"


def ensure_downloads_folder():
    """Ensure the downloads folder exists"""
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)


def load_json(filepath: str) -> dict:
    """Load and return JSON content"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"ERROR: File not found → {filepath}")
    except json.JSONDecodeError:
        sys.exit(f"ERROR: Invalid JSON format → {filepath}")


def download_mp3(url: str, title: str):
    """Download a YouTube video as MP3 using yt_dlp"""
    outtmpl = os.path.join(DOWNLOADS_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": False,
    }

    print(f"\nDownloading: {title}")
    print(f"URL: {url}")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")

    except Exception as e:
        print(f"ERROR downloading '{title}': {e}", file=sys.stderr)


def download_all_videos(json_path: str):
    """Read JSON and download all videos in MP3 format"""
    ensure_downloads_folder()

    data = load_json(json_path)
    videos = data.get("videos", [])

    print(f"\nPlaylist: {data.get('playlist_title')}")
    print(f"Videos to download: {len(videos)}")
    print("-" * 50)

    for video in videos:
        url = video.get("url")
        title = video.get("title")

        if not url:
            print("Skipping video with missing URL")
            continue

        download_mp3(url, title)

    print("\nAll downloads finished!")


if __name__ == "__main__":
    # You can change the filename here if needed
    download_all_videos("downloads/videos_info.json")
