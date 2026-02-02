# BridgeMeet

BridgeMeet is an accessibility-focused video communication platform designed to bridge communication gaps between users who rely on different communication modalities such as speech, text, and sign language.

This repository currently contains the speech recognition module of the system, which enables converting spoken audio into English text using AI-based speech-to-text models. This module forms the foundation for live captions in the larger BridgeMeet platform.

---

## Current Capabilities

- Microphone-based audio recording
- Speech-to-text transcription using OpenAI Whisper
- Automatic translation of spoken language into English
- Timestamped transcription segments

---

## Planned Capabilities

- Real-time live captions in video meetings
- Text-to-speech synthesis
- AI-assisted sign language recognition (prototype-level)
- Multimodal communication support

---

## Technology Stack

- Python 3.9+
- OpenAI Whisper
- PyTorch
- SpeechRecognition
- PyAudio
- FFmpeg
- PortAudio

---

## System Requirements

### Linux (Ubuntu / Debian)

sudo apt update  
sudo apt install -y ffmpeg portaudio19-dev

### macOS

brew install ffmpeg portaudio

### Windows

- Install FFmpeg and add it to PATH
- Install PortAudio
- Install PyAudio using a compatible wheel

---

## Python Setup

git clone https://github.com/dhanesh221/BridgeMeet.git  
cd BridgeMeet  

python3 -m venv venv  
source venv/bin/activate  

pip install -r requirements.txt

---

## Usage

python MainRecordAudio.py

---

## Limitations

- Batch transcription only
- No real-time streaming yet
- Sign language recognition not integrated

---

## License

Educational and research use only.
