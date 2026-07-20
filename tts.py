import edge_tts
import asyncio
import os


async def generate_speech(text):
    os.makedirs("audio", exist_ok=True)

    output_file = "audio/english_audio.mp3"

    print("Generating English speech...")

    voice = "en-US-AriaNeural"

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(output_file)

    print("Saved:", output_file)

    return output_file


def text_to_speech(text):
    asyncio.run(generate_speech(text))

    return "audio/english_audio.mp3"