import subprocess
import os

def extract_audio(video_path):
    os.makedirs("audio", exist_ok=True)

    output_audio = "audio/audio.wav"

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        "-y",
        output_audio
    ]

    print("Extracting audio...")

    subprocess.run(command, check=True)

    print("Audio extracted successfully!")

    return output_audio