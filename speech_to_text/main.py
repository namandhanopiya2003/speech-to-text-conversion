import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import argparse
from config.config import load_config
from models.wav2vec_model import Wav2Vec2SpeechRecognizer
from models.whisper_model import WhisperSpeechRecognizer
from models.custom_model import CustomSpeechRecognizer
from preprocessing.audio_processing import preprocess_audio
from utils.record_audio import record_audio
from utils.helpers import save_transcription

def get_model(model_type, model_name):
    if model_type == "wav2vec2":
        return Wav2Vec2SpeechRecognizer(model_name)
    elif model_type == "whisper":
        return WhisperSpeechRecognizer(model_name)
    elif model_type == "custom":
        return CustomSpeechRecognizer(model_name)
    else:
        raise ValueError(f"Unknown model type: {model_type}")

def main(audio_path=None, use_mic=False):
    config = load_config()

    if use_mic:
        print("Recording from microphone...")
        recorded_file = record_audio(
            filename="mic_recording.wav",
            duration=config.get("record_duration", 5),            
            fs=config.get("sample_rate", 16000),                
            folder="audio_samples/mic_recordings" 
        )
        audio, sr = preprocess_audio(recorded_file)
    elif audio_path:
        audio, sr = preprocess_audio(audio_path)
    else:
        raise ValueError("Either --audio or --mic must be provided.")

    recognizer = get_model(config["model_type"], config["model_name"])

    print("Transcribing audio...")
    transcription = recognizer.transcribe(audio, sr)

    print("Transcription Result:")
    print(transcription)

    if config.get("save_transcript", False):
        output_path = config.get("output_text_file", "transcript.txt")
        save_transcription(transcription, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Speech to Text Transcription")
    parser.add_argument('--audio', type=str, help="Path to audio file")
    parser.add_argument('--mic', action='store_true', help="Use microphone for input")
    args = parser.parse_args()

    main(audio_path=args.audio, use_mic=args.mic)
