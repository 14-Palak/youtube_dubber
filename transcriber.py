import whisper
import os

def transcribe_audio(audio_path):
    os.makedirs("transcript", exist_ok=True)

    print("Loading Whisper model...")

    model = whisper.load_model("base")

    print("Transcribing audio...")

    result = model.transcribe(audio_path)

    text = result["text"]

    with open("transcript/transcript.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Transcription completed!")

    return text