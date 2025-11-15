from dotenv import load_dotenv
import os
import json
from yt_dlp import YoutubeDL


def load_playlist_url() -> str:
    """Load the playlist URL form the .env file"""
    load_dotenv()  # Loads variables from .env
    playlist_url = os.getenv('PLAYLIST_URL')

    if not playlist_url:
        raise ValueError("PLAYLIST_URL is not set in the .env file")

    return playlist_url


def fetch_playlist_data(playlist_url: str) -> dict:
    """Fetch playlist metadata from YouTube using yt-dpl"""
    yt_opts = {"quiet": True, "extract_flat": True}

    with YoutubeDL(yt_opts) as ydl:
        playlist_dict = ydl.extract_info(playlist_url, download=False)

    return playlist_dict


def build_json_structure(playlist_dict: dict) -> dict:
    """Convert yt-dlp playlist metadata into a clean JSON-ready structure"""
    videos = [
        {
            "title": entry.get("title"),
            "url": f"https://www.youtube.com/watch?v={entry.get('id')}"
        }
        for entry in playlist_dict.get("entries", [])
    ]

    return {
        "playlist_title": playlist_dict.get("title"),
        "number_of_videos": len(videos),
        "videos": videos
    }


def save_json(data: dict, filename: str = "videos_info.json") -> None:
    """Save dictionary data as a JSON file inside the ./downloads folder"""

    base_dir = os.path.dirname(os.path.abspath(
        __file__))  # directory of main.py
    downloads_dir = os.path.join(base_dir, "downloads")

    # Create the folder if it doesn't exist
    os.makedirs(downloads_dir, exist_ok=True)

    filepath = os.path.join(downloads_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"JSON saved successfully")


def main():
    try:
        playlist_url = load_playlist_url()
        playlist_data = fetch_playlist_data(playlist_url)

        json_data = build_json_structure(playlist_data)
        save_json(json_data)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
