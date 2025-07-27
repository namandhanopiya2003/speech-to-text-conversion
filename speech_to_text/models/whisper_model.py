import whisper

class WhisperSpeechRecognizer:
    def __init__(self, model_size="base"):
        # Loads a pre-trained Whisper model (default set as "base")
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path):
        # Transcribes the speech from the audio file
        result = self.model.transcribe(audio_path)

        # Returns only the text part from the result
        return result["text"]
