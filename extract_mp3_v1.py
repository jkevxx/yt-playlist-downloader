import yt_dlp
import sys


def download_youtube_as_mp3():
    url = 'https://www.youtube.com/watch?v=P9iy6wjbOiQ'
    output_template = 'downloads/%(title)s.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',  # Bitrate in kbps
        }],
        'quiet': False,  # Set to True to suppress console output
    }

    try:
        print(f"Starting download for URL: {url}")
        # Create a YoutubeDL object with the specified options and download the audio.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("\n✅ Download complete!")
        print("Your file has been saved in the 'downloads' folder.")

    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        print("Please check the URL and your internet connection.")


download_youtube_as_mp3()
