# Import necessary libraries
import torch
import torch.nn as nn
import torchaudio
import torchaudio.transforms as T

# Defined a custom speech recognition model using CNN + LSTM + Linear layers
class SpeechRecognitionModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SpeechRecognitionModel, self).__init__()

        # CNN (convolutional neural network) to extract features from audio
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        # LSTM layer to capture the sequence/timing of spoken words
        self.lstm = nn.LSTM(input_size=32 * 39, hidden_size=hidden_dim, num_layers=2, batch_first=True)

        # Final linear layer to convert model output to letter predictions
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        batch_size, time, features = x.size()
        x = x.view(batch_size, 1, time, features)
        x = self.cnn(x)
        x = x.permute(0, 2, 1, 3).contiguous().view(batch_size, -1, 32 * 39)
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

# This class handles the full speech recognition process using above model
class CustomSpeechRecognizer:

    # Sets up the speech model and the characters it can recognize
    def __init__(self):
        self.labels = "_'ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.model = SpeechRecognitionModel(input_dim=128, hidden_dim=256, output_dim=len(self.labels))
        self.model.eval()

    # Converts an audio file into a format the model can understand
    def preprocess_audio(self, audio_path):
        waveform, sample_rate = torchaudio.load(audio_path)
        transform = T.MelSpectrogram(sample_rate=sample_rate, n_mels=128)
        mel_spec = transform(waveform).squeeze(0).transpose(0, 1)
        return mel_spec.unsqueeze(0)

    # Turns the model’s prediction (numbers) into readable text
    def decode_output(self, output_tensor):
        predicted_indices = torch.argmax(output_tensor, dim=-1)
        return ''.join([self.labels[idx] for idx in predicted_indices])

    # Takes an audio file and returns the spoken text as a string
    def transcribe(self, audio_path):
        input_tensor = self.preprocess_audio(audio_path)
        with torch.no_grad():
            output = self.model(input_tensor)
        transcription = self.decode_output(output)
        return transcription
