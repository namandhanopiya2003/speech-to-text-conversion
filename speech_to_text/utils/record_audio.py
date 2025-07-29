import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="mic_recording.wav", duration=5, fs=16000, folder="audio_samples/mic_recordings"):
    print(f"Recording for {duration} seconds...")

    # Records audio from microphone
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Creates folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Creates full path for saving
    filepath = os.path.join(folder, filename)

    # Saves recorded audio to WAV file
    write(filepath, fs, audio)
    
    print(f"Saved recording: {filepath}")
    # Returns path to the saved audio
    return filepath
