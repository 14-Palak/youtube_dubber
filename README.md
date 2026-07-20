# 🎬 Automated Video Dubbing System

An AI-powered application that downloads a YouTube video, transcribes its speech, translates the text to English, generates English speech, and creates a dubbed video.

## ✨ Features

- Download YouTube videos
- Extract audio using FFmpeg
- Speech-to-text using OpenAI Whisper
- Translate text to English
- Generate English speech using Edge TTS
- Merge translated audio with the original video

## 🛠️ Technologies Used

- Python
- OpenAI Whisper
- Edge TTS
- yt-dlp
- FFmpeg
- deep-translator

## 📁 Project Structure

```
youtube_dubber/
│── main.py
│── downloader.py
│── audio.py
│── transcriber.py
│── translator.py
│── tts.py
│── merger.py
│── requirements.txt
│── README.md
│
├── videos/
├── audio/
├── output/
└── transcript/
```

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/youtube_dubber.git

cd youtube_dubber

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## ▶️ Run

```bash
python main.py
```

Enter a YouTube URL when prompted.

## 📦 Output

The final dubbed video is saved in:

```
output/dubbed_video.mp4
```

## 👩‍💻 Author

Palak Digarse