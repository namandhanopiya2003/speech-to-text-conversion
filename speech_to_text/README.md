## Speech-to-text project

## 🧠 ABOUT THIS PROJECT ==>

- This is a Python-based Speech-to-Text transcription system that supports audio input via microphone recording or existing audio files. It uses state-of-the-art speech recognition models such as Wav2Vec2, Whisper, and a custom model for transcribing spoken audio into text.

- The project includes preprocessing of audio, model selection based on configuration, real-time microphone recording, and saving transcriptions to a file.

- Ideal for academic demos, prototyping, voice command systems, or integration into larger AI/assistive technologies.

---

## ⚙ TECHNOLOGIES USED ==>

- **Python**

- **PyTorch** (for deep learning model inference)

- **Transformers** (Hugging Face library for Wav2Vec2 and Whisper models)

- **Librosa** (audio preprocessing)

- **Sounddevice** (for microphone recording)

- **Numpy**

- **ConfigParser / YAML** (for configuration management)

---

## 📁 PROJECT FOLDER STRUCTURE ==>

speech_to_text_project/
├── audio_samples/                              # Sample audio files for testing
│ ├── mic_recordings/
│ └── sample.wav
│ 
├── config/
│ ├── _init_.py
│ ├── config.yaml
│ └── config.py                                 # Configuration loader (model type, sample rate, etc.)
│
├── main.py                                     # Main entry point script for running transcription
│
├── models/
│ ├── _init_.py
│ ├── wav2vec_model.py                          # Wav2Vec2 speech recognition model wrapper
│ ├── whisper_model.py                          # Whisper speech recognition model wrapper
│ └── custom_model.py                           # Custom model wrapper (if any)
│
├── preprocessing/
│ ├── _init_.py
│ └── audio_processing.py                       # Functions for preprocessing and mic recording
│
├── utils/
│ ├── _init_.py
│ ├── helpers.py                                # Helper functions like saving transcription, recording audio
│ └── record_audio.py                           # Audio recording utilities
│
├── transcript.txt                              # Output transcription file (generated after running)
├── requirements.txt                            # Python dependencies list
└── README.md                                   # Project documentation

---

## 📝 WHAT EACH FILE DOES ==>

**main.py**:
- Parses command line arguments (--mic or --audio <file>)
- Loads configuration
- Records audio from mic or loads audio file
- Selects appropriate speech recognition model
- Performs transcription and prints output
- Saves transcription to file

**config/config.py**:
- Loads user configuration such as model type, model name, sample rate, and output path.

**models/**:
- Contains wrapper classes for different speech recognition models, abstracting loading and inference logic.

**preprocessing/audio_processing.py**:
- Functions for audio preprocessing and microphone audio capture.

**utils/helpers.py**:
- Utility functions, including saving transcriptions and auxiliary helpers.

**utils/record_audio.py**:
- Handles low-level microphone recording functionality.

**audio_samples/**:
- Folder containing example audio files for testing transcription.

---

## 🚀 HOW TO RUN ==>

- Open cmd and run following commands ->

# Step 1: Navigate to your project directory
cd D:\speech_to_text_project
D:

# Step 2: Install required dependencies
pip install -r requirements.txt

# Step 3: Run transcription from microphone
python main.py --mic

# OR

# Step 3 (alternative): Run transcription from an audio file
python main.py --audio audio_samples/sample.wav

---

## ✨ SAMPLE OUTPUT ==>

Recording from microphone...
Recording for 5 seconds...
Saved recording: audio_samples/mic_recordings/mic_recording.wav
Transcribing audio...
Transcription Result:
hallo how are you
Transcript saved to transcript.txt

---

## 📬 CONTACT ==>

For questions or feedback, feel free to reach out!

---
