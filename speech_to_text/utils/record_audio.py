import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="mic_recording.wav", duration=5, fs=16000, folder="audio_samples/mic_recordings"):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    write(filepath, fs, audio)
    print(f"Saved recording: {filepath}")
    return filepath
