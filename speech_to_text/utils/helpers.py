import os

def save_transcription(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Transcript saved to {output_path}")
