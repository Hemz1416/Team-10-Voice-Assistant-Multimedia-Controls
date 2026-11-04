import json
from unittest.mock import MagicMock, patch

import pytest

from src.speech_input import SpeechInput


def test_speech_input_missing_model(tmp_path):
    missing = tmp_path / "nonexistent_model"
    with pytest.raises(FileNotFoundError, match="Vosk model folder not found"):
        SpeechInput(model_path=str(missing))


@patch("src.speech_input.Model")
def test_speech_input_init_success(mock_model, tmp_path):
    model_dir = tmp_path / "dummy_model"
    model_dir.mkdir()

    speech = SpeechInput(model_path=str(model_dir), sample_rate=8000, recording_seconds=2)
    assert speech.sample_rate == 8000
    assert speech.recording_seconds == 2
    mock_model.assert_called_once_with(str(model_dir))


@patch("src.speech_input.KaldiRecognizer")
@patch("src.speech_input.sd")
@patch("src.speech_input.Model")
def test_speech_input_listen_and_transcribe_success(mock_model, mock_sd, mock_recognizer_cls, tmp_path):
    model_dir = tmp_path / "dummy_model"
    model_dir.mkdir()

    dummy_audio = MagicMock()
    dummy_audio.tobytes.return_value = b"\x00" * 32000
    mock_sd.rec.return_value = dummy_audio

    mock_rec_instance = MagicMock()
    mock_rec_instance.FinalResult.return_value = json.dumps({
        "text": "play",
        "result": [{"conf": 0.95, "word": "play"}]
    })
    mock_recognizer_cls.return_value = mock_rec_instance

    speech = SpeechInput(model_path=str(model_dir))
    res = speech.listen_and_transcribe()

    assert res["text"] == "play"
    assert res["confidence"] == pytest.approx(0.95)
    mock_sd.rec.assert_called_once()
    mock_sd.wait.assert_called_once()


@patch("src.speech_input.KaldiRecognizer")
@patch("src.speech_input.sd")
@patch("src.speech_input.Model")
def test_speech_input_listen_empty_words(mock_model, mock_sd, mock_recognizer_cls, tmp_path):
    model_dir = tmp_path / "dummy_model"
    model_dir.mkdir()

    dummy_audio = MagicMock()
    dummy_audio.tobytes.return_value = b"\x00" * 16000
    mock_sd.rec.return_value = dummy_audio

    mock_rec_instance = MagicMock()
    mock_rec_instance.FinalResult.return_value = json.dumps({
        "text": "",
        "result": []
    })
    mock_recognizer_cls.return_value = mock_rec_instance

    speech = SpeechInput(model_path=str(model_dir))
    res = speech.listen_and_transcribe()

    assert res["text"] == ""
    assert res["confidence"] is None
