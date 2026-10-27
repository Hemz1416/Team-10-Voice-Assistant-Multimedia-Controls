
import json
from pathlib import Path

import sounddevice as sd
from vosk import KaldiRecognizer, Model


class SpeechInput:
    def __init__(
        self,
        model_path="models/vosk-model-small-en-us-0.15",
        sample_rate=16000,
        recording_seconds=5,
    ):
        model_dir = Path(model_path)

        if not model_dir.is_dir():
            raise FileNotFoundError(
                f"Vosk model folder not found: {model_dir}"
            )

        self.model = Model(str(model_dir))
        self.sample_rate = sample_rate
        self.recording_seconds = recording_seconds

    def listen_and_transcribe(self):
        print("Listening... Speak a media command.")

        audio = sd.rec(
            int(self.recording_seconds * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
        )
        sd.wait()

        recognizer = KaldiRecognizer(
            self.model, self.sample_rate
        )
        recognizer.SetWords(True)

        recognizer.AcceptWaveform(audio.tobytes())
        result = json.loads(recognizer.FinalResult())

        text = result.get("text", "").strip()
        words = result.get("result", [])

        confidence = (
            sum(word["conf"] for word in words) / len(words)
            if words else None
        )

        print(f"Recognized speech: {text or '(no speech recognized)'}")

        return {
            "text": text,
            "confidence": confidence,
        }


if __name__ == "__main__":
    speech = SpeechInput()
    print(speech.listen_and_transcribe())
