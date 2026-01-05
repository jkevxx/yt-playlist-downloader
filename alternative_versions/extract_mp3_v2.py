from yt_dlp import YoutubeDL


def download_youtube_as_mp3():

    download_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",  # output file name
        "player_client": "web",       # ✅ important workaround
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "128",
            }
        ],
    }

    with YoutubeDL(download_opts) as ydl:
        video_url = "https://www.youtube.com/watch?v=P9iy6wjbOiQ"
        ydl.download([video_url])


download_youtube_as_mp3()
print("✅ audio downloaded")
