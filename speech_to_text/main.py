# Setting up imports and path
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

# Function that selects the correct model based on config
def get_model(model_type, model_name):
    if model_type == "wav2vec2":
        return Wav2Vec2SpeechRecognizer(model_name)
    elif model_type == "whisper":
        return WhisperSpeechRecognizer(model_name)
    elif model_type == "custom":
        return CustomSpeechRecognizer(model_name)
    else:
        raise ValueError(f"Unknown model type: {model_type}")

# Main function to handle audio input and transcription
def main(audio_path=None, use_mic=False):
    config = load_config()

    # To record audio using microphone
    if use_mic:
        print("Recording from microphone...")

        # Records live audio and saves it
        recorded_file = record_audio(
            filename="mic_recording.wav",
            duration=config.get("record_duration", 5),           # Default: 5 seconds            
            fs=config.get("sample_rate", 16000),                 # Default: 16kHz sample rate                
            folder="audio_samples/mic_recordings" 
        )

        # It preprocess the recorded audio (e.g., resample, normalize)
        audio, sr = preprocess_audio(recorded_file)

    # When we use an existing audio file path
    elif audio_path:
        # It preprocess the given audio file
        audio, sr = preprocess_audio(audio_path)
        
    else:
        # Gives an error, if neither mic nor audio file is given
        raise ValueError("Either --audio or --mic must be provided.")

    # It loadS the appropriate model for transcription
    recognizer = get_model(config["model_type"], config["model_name"])

    print("Transcribing audio...")
    # Performs speech recognition on the audio
    transcription = recognizer.transcribe(audio, sr)

    # It prints the result on the screen
    print("Transcription Result:")
    print(transcription)

    # Saves the result
    if config.get("save_transcript", False):
        output_path = config.get("output_text_file", "transcript.txt")
        save_transcription(transcription, output_path)

if __name__ == "__main__":

    # Creates a parser to read inputs
    parser = argparse.ArgumentParser(description="Speech to Text Transcription")
    # It adds option to give an audio file
    parser.add_argument('--audio', type=str, help="Path to audio file")
    # It adds option to let user choose microphone input instead
    parser.add_argument('--mic', action='store_true', help="Use microphone for input")
    # It reads and understands what is typed in the terminal
    args = parser.parse_args()

    # Main function is called and given user's choices
    main(audio_path=args.audio, use_mic=args.mic)
