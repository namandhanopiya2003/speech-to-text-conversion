import librosa
import numpy as np
import soundfile as sf
import sounddevice as sd
import scipy.io.wavfile as wav
import os

def load_audio(file_path, target_sr=16000):

    # Loads audio file and resample to target sample rate
    audio, sr = librosa.load(file_path, sr=target_sr)
    return audio, sr

def normalize_audio(audio):
    # Normalizes volume to make the sound consistent
    return librosa.util.normalize(audio)

def save_audio(audio, sr, output_path):
    # Saves audio data to file in WAV format
    sf.write(output_path, audio, sr)

# Loads an audio file and normalizes its volume to prepare it for further processing
def preprocess_audio(file_path):
    audio, sr = load_audio(file_path)
    audio = normalize_audio(audio)
    return audio, sr

def record_from_mic(duration=5, sample_rate=16000, output_path="recorded.wav"):
    print(f"[INFO] Recording for {duration} seconds...")

    # Records audio using microphone for the given duration and sample rate
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()                                                       

    # Creates folder if it doesn’t exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Saves the recorded audio to a WAV file
    wav.write(output_path, sample_rate, audio)
    print(f"[INFO] Recording saved to: {output_path}")

    # Returns the path where the audio is saved
    return output_path
