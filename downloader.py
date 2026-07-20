import yt_dlp
import os


def download_video(url):
    os.makedirs("videos", exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio",
        "outtmpl": "videos/input.%(ext)s",
        "merge_output_format": "mp4",
        "noplaylist": True,
    }

    print("Downloading video with audio...")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Download completed!")