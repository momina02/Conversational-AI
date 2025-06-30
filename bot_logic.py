import webrtcvad
import pyaudio
import wave
import whisper
from groq import Groq
import edge_tts
import asyncio
import os
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.playback import play

load_dotenv()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 480
VAD_MODE = 2

def record_audio():
    vad = webrtcvad.Vad(VAD_MODE)
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []
    silence_counter = 0
    silence_threshold = 15
    min_speech_chunks = 10

    print("🎙️ سننے کے لیے تیار ہوں...")

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        is_speech = vad.is_speech(data, RATE)
        print(f"{'🔊 بول رہے ہیں' if is_speech else '🤫 خاموشی'}")

        if is_speech:
            frames.append(data)
            silence_counter = 0
        else:
            if len(frames) >= min_speech_chunks:
                silence_counter += 1
                if silence_counter >= silence_threshold:
                    break

    stream.stop_stream()
    stream.close()
    pa.terminate()

    filename = "input.wav"
    wf = wave.open(filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return filename

def transcribe_audio(audio_file):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language="ur")
        return result["text"]
    except Exception as e:
        print(f"⚠️ Transcription error: {e}")
        return ""

def generate_response(text):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "آپ اردو زبان کے ماہر استاد ہیں۔ آپ صرف اردو زبان میں گرامر، تلفظ، لغت، اور جملوں کی ساخت کے بارے میں سادہ اور واضح انداز میں تعلیم دیتے ہیں۔ آپ انگریزی یا کسی بھی غیر اردو زبان کا کوئی لفظ استعمال نہیں کرتے۔ اگر صارف انگریزی میں سوال کرے تو آپ اردو میں ہی جواب دیں گے اور درخواست کریں گے کہ وہ اردو میں بات کریں۔ آپ ہر سوال کا جواب اردو زبان میں دیں گے، چاہے سوال کسی بھی زبان میں ہو۔"},
                {"role": "user", "content": text}
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"⚠️ Groq error: {e}")
        return ""

async def text_to_speech(text):
    try:
        output_file = "output.mp3"
        communicate = edge_tts.Communicate(text, "ur-PK-AsadNeural")
        await communicate.save(output_file)
        return output_file
    except Exception as e:
        print(f"⚠️ TTS Error: {e}")
        return ""

def play_audio(audio_file):
    try:
        if os.path.exists(audio_file):
            audio = AudioSegment.from_mp3(audio_file)
            play(audio)
    except Exception as e:
        print(f"⚠️ Play error: {e}")
