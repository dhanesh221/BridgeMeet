import whisper
import speech_recognition as sr
import tempfile
import os

# -----------------------------
# Setup
# -----------------------------
model = whisper.load_model("medium")  # medium is too slow for realtime
r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = True

print("Listening... Press Ctrl+C to stop")

# -----------------------------
# Real-time loop
# -----------------------------
with sr.Microphone(sample_rate=16000) as source:
    while True:
        try:
            audio = r.listen(source, phrase_time_limit=3)

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                f.write(audio.get_wav_data())
                audio_path = f.name

            result = model.transcribe(
                audio_path,
                fp16=False,
                language="en"
            )

            text = result["text"].strip()
            if text:
                print("🗣️", text)

            os.remove(audio_path)

        except KeyboardInterrupt:
            print("\nStopping.")
            break
