from merger import merge_audio
from tts import text_to_speech
from downloader import download_video
from audio import extract_audio
from transcriber import transcribe_audio
from translator import translate_text
import os


def main():
    print("=" * 50)
    print("YouTube Video Dubber")
    print("=" * 50)

    url = input("Enter YouTube URL: ")

    # Download video
    download_video(url)

    # Find downloaded video
    video_file = None

    for file in os.listdir("videos"):
        if file.endswith((".mp4", ".webm", ".mkv")):
            video_file = os.path.join("videos", file)
            break

    if video_file:
        # Extract audio
        audio_file = extract_audio(video_file)

        # Transcribe
        text = transcribe_audio(audio_file)

        print("\n========== ORIGINAL TEXT ==========\n")
        print(text)

        # Translate
        english_text = translate_text(text)

        print("\n========== ENGLISH ==========\n")
        print(english_text)

# Convert translated text to speech
        english_audio = text_to_speech(english_text)

        print("VIDEO FILE:", video_file)
        print("AUDIO FILE:", english_audio)

        merge_audio(video_file, english_audio)

        print(f"\nEnglish audio saved at: {english_audio}")

    else:
        print("No video found.")


if __name__ == "__main__":
    main()