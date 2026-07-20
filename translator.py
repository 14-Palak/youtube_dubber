from deep_translator import GoogleTranslator
import os


def translate_text(text):
    os.makedirs("transcript", exist_ok=True)

    print("Translating to English...")

    translated_text = GoogleTranslator(
        source="auto",
        target="en"
    ).translate(text)

    with open("transcript/translated.txt", "w", encoding="utf-8") as file:
        file.write(translated_text)

    print("Translation completed!")

    return translated_text