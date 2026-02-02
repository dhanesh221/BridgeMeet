import whisper
import speech_recognition as sr
import os

# -----------------------------
# Configuration
# -----------------------------
SAMPLE_RATE = 16000
RECORD_SECONDS = 10
AUDIO_FILE = "input.wav"

# -----------------------------
# Record Audio
# -----------------------------
r = sr.Recognizer()

with sr.Microphone(sample_rate=SAMPLE_RATE) as source:
    print("Recording... Speak naturally.")
    audio = r.record(source, duration=RECORD_SECONDS)

with open(AUDIO_FILE, "wb") as f:
    f.write(audio.get_wav_data())

# -----------------------------
# Load Whisper
# -----------------------------
print("Loading Whisper model...")
model = whisper.load_model("medium")

# -----------------------------
# Canonical transcription (English)
# -----------------------------
print("Transcribing + translating to English...")

result = model.transcribe(
    AUDIO_FILE,
    task="translate",   # 🔴 THIS IS THE KEY
    fp16=False,
    temperature=0.0
)

english_text = result["text"].strip()

print("\n--- Canonical English Text ---")
print(english_text)

# -----------------------------
# (Optional) Subtitle timing
# -----------------------------
print("\n--- Timed Segments ---")
for seg in result["segments"]:
    print(f"[{seg['start']:.2f} – {seg['end']:.2f}] {seg['text']}")

# -----------------------------
# Cleanup
# -----------------------------
os.remove(AUDIO_FILE)
