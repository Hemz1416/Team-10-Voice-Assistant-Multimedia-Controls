import pytest

from src.intent_processor import detect_intent


@pytest.mark.parametrize(
    ("phrase", "expected"),
    [
        ("please play music", "PLAY"),
        ("could you please play music", "PLAY"),
        ("can you pause music", "PAUSE"),
        ("next song", "NEXT"),
        ("turn the volume up", "VOLUME_UP"),
        ("turn the volume down", "VOLUME_DOWN"),
        ("turn volume up", "VOLUME_UP"),
        ("please mute audio", "MUTE"),
        ("could you stop playback", "STOP"),
        ("dont play music", None),
        ("play music and stop", None),
        ("open browser", None),
    ],
)
def test_intent_variations(phrase, expected):
    assert detect_intent(phrase).intent == expected