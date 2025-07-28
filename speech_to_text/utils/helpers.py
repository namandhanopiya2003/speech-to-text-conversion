import os

# The function saves the transcribed text in a file at the given location
def save_transcription(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:

        # Writes the text into the file
        f.write(text)

    # Prints that the file was saved with path
    print(f"Transcript saved to {output_path}")
