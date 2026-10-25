
from src.intent_processor import detect_intent


def test_play_command():
    assert detect_intent("play")["intent"] == "PLAY"


def test_play_music_command():
    assert detect_intent("play music")["intent"] == "PLAY"


def test_pause_command():
    assert detect_intent("please pause")["intent"] == "PAUSE"


def test_case_and_whitespace():
    assert detect_intent("  PLAY MUSIC  ")["intent"] == "PLAY"


def test_unsupported_command():
    assert detect_intent("tell me a joke")["intent"] is None


def test_empty_command():
    assert detect_intent("")["intent"] is None
