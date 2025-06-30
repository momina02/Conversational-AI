# 🎙️ AI Text-to-Speech Assistant with Edge-TTS

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Text-to-Speech](https://img.shields.io/badge/TTS-Edge--TTS-orange)

Convert any text into realistic human speech using Microsoft's **Edge TTS** voice synthesis, and instantly play it using Python.

---

## ✨ Features

- 🔊 Convert text to high-quality MP3 speech
- 🧠 Uses Microsoft Neural voices (e.g. `en-US-JennyNeural`)
- 🎧 Plays audio instantly using `playsound`
- 💡 Simple and async-friendly architecture
- 📦 Lightweight with minimal dependencies

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-text-to-speech.git
cd ai-text-to-speech
pip install -r requirements.txt
````

Or install individually:

```bash
pip install edge-tts playsound
```

---

## 🚀 Usage

```bash
python text_to_speech.py
```

This will:

1. Convert your sample text into `output.mp3`
2. Play the MP3 using your default audio output

---

## 🗣️ Available Voices

You can choose from dozens of voices and languages provided by Microsoft. Example voice IDs:

* `en-US-JennyNeural` (Female)
* `en-US-GuyNeural` (Male)
* `ur-PK-AsadNeural` (Male, Urdu)
* `hi-IN-SwaraNeural` (Female, Hindi)

Full list: [https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support#neural-voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support#neural-voices)

---

## 📂 Project Structure

```
📁 ai-text-to-speech/
├── text_to_speech.py
├── output.mp3
└── README.md
```

## 📝 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for more details.

---

## 🙌 Credits

* [Microsoft Edge TTS](https://github.com/rany2/edge-tts)
* [playsound](https://github.com/TaylorSMarks/playsound)

---

## 🧠 Future Ideas

* GUI with Tkinter or PyQt
* Integrate with ChatGPT for dynamic conversation
* Support for multiple languages and input files

