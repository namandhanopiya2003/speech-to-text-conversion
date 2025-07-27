from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torch
import torchaudio

class Wav2Vec2SpeechRecognizer:
    def __init__(self, model_name):
        # Loads a pre-trained tokenizer and model using the model's name
        self.tokenizer = Wav2Vec2Tokenizer.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)

    def transcribe(self, audio_array, sample_rate):
        # Resamples the audio sample rate if not 16000 Hz (as required by model)
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            audio_array = resampler(torch.tensor(audio_array))
        else:
            # Converts to tensor if already correct sample rate
            audio_array = torch.tensor(audio_array)

        # Tokenize the audio, run it through the model, get the most likely predictions, and convert them into readable text
        input_values = self.tokenizer(audio_array.squeeze().numpy(), return_tensors="pt", padding="longest").input_values
        logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.tokenizer.decode(predicted_ids[0])
        return transcription.lower()
