# 🧠 Urdu Conversational AI Bot 🎙️🤖

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Text-to-Speech](https://img.shields.io/badge/TTS-Edge--TTS-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)
![Speech-to-Text](https://img.shields.io/badge/STT-Whisper-blueviolet)
![Speech-Detection](https://img.shields.io/badge/Voice-VAD--webrtc-yellowgreen)
![LLM](https://img.shields.io/badge/LLM-Groq%20%2F%20LLaMA4-red)


Welcome to the **Urdu Conversational AI Bot** — an intelligent voice assistant that listens to your voice, understands Urdu speech, responds using advanced AI, and replies back in audio — all in **pure Urdu language** 🇵🇰🗣️🔊

---

## 🚀 Features

- 🎤 **Voice Activated**: Starts listening automatically and stops when you're done.
- 🧠 **LLM Powered**: Uses [Groq API](https://groq.com/) with **Meta-LLaMA 4** model.
- 🗣️ **Speech to Text**: Transcribes Urdu speech using [OpenAI Whisper](https://github.com/openai/whisper).
- 🗨️ **AI Chat**: Intelligent Urdu-only conversation based on your input.
- 🔈 **Text to Speech**: Replies using Urdu neural voice (`ur-PK-AsadNeural`) with [Edge TTS](https://github.com/rany2/edge-tts).
- 🧏 **Polite Behavior**: Ends conversation on words like _"خدا حافظ"_ or _"الوداع"_.
- 🛠️ **API Ready**: Easily extendable with [FastAPI](https://fastapi.tiangolo.com/).

---

## 📂 Project Structure

```

📦 UrduBot
├── bot\_logic.py        # Core bot logic: record, transcribe, respond, TTS, playback
├── main.py             # FastAPI server with `/start-call` endpoint
├── .env                # Environment variables (API keys)
└── requirements.txt    # Required Python libraries

````

---

## 🧪 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/urdu-conversational-bot.git
cd urdu-conversational-bot
````

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root directory and add your API key:

```
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Bot

### 1. Start the API

```bash
uvicorn main:app --reload
```

### 2. Visit the Endpoint

Navigate to:

```
http://127.0.0.1:8000/start-call
```

Your bot will begin recording your Urdu speech and start a conversation 🧠🔁🎧

---

## 💻 Example Workflow

1. You say: *"مجھے اردو گرامر کے بارے میں بتائیں"*
2. ✅ Bot transcribes it.
3. 🤖 Bot generates a detailed Urdu explanation.
4. 🔊 Bot speaks the answer in a natural Urdu voice.

---

## 🧰 Tech Stack

| Component        | Technology             |
| ---------------- | ---------------------- |
| Speech Detection | `webrtcvad`, `pyaudio` |
| Transcription    | `openai-whisper`       |
| AI Response      | `Groq` with LLaMA 4    |
| TTS              | `edge-tts`             |
| Playback         | `pydub`                |
| API              | `FastAPI`              |

---

## 📌 Exit Condition

Say one of the following to end the conversation gracefully:

* *"خدا حافظ"*
* *"الوداع"*

---

## ❗ Troubleshooting

* Make sure your microphone is connected and not muted.
* Use clear Urdu speech for better accuracy.
* If you see errors like `TTS Error`, check internet or Edge TTS compatibility.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.

---

## 🙏 Acknowledgements

* [OpenAI Whisper](https://github.com/openai/whisper)
* [Groq](https://groq.com/)
* [Edge TTS](https://github.com/rany2/edge-tts)
* [FastAPI](https://fastapi.tiangolo.com/)

---

## 🌟 Star the repo if you like it!
