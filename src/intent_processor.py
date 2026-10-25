
import re


COMMAND_PHRASES = {
    "PLAY": [
        "play",
        "play music",
        "start playing",
    ],
    "PAUSE": [
        "pause",
        "pause music",
        "please pause",
    ],
    "RESUME": [
        "resume",
        "resume music",
        "continue playing",
    ],
    "STOP": [
        "stop",
        "stop music",
    ],
    "NEXT": [
        "next",
        "next track",
        "next song",
    ],
    "PREVIOUS": [
        "previous",
        "previous track",
        "previous song",
    ],
    "VOLUME_UP": [
        "volume up",
        "increase volume",
        "turn volume up",
    ],
    "VOLUME_DOWN": [
        "volume down",
        "decrease volume",
        "turn volume down",
    ],
    "MUTE": [
        "mute",
        "mute audio",
        "mute the sound",
    ],
}


def normalize_text(text):
    text = text.lower().strip()
    return re.sub(r"\s+", " ", text)


def detect_intent(text, confidence=None):
    phrase = normalize_text(text or "")

    for intent, phrases in COMMAND_PHRASES.items():
        if phrase in phrases:
            return {
                "intent": intent,
                "confidence": confidence,
                "recognized_text": phrase,
            }

    return {
        "intent": None,
        "confidence": confidence,
        "recognized_text": phrase,
    }
