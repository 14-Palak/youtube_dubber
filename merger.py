import subprocess
import os


def merge_audio(video_path, audio_path):

    os.makedirs("output", exist_ok=True)

    output = "output/dubbed_video.mp4"

    print("Merging video and English audio...")

    command = [
        "ffmpeg",
        "-i", video_path,
        "-i", audio_path,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "libx264",
        "-preset", "fast",
        "-c:a", "aac",
        "-b:a", "128k",
        "-y",
        output
    ]

    subprocess.run(command)

    print("✅ Final dubbed video created!")
    print(output)