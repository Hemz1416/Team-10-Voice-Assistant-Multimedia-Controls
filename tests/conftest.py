import sys
from unittest.mock import MagicMock

# Gracefully provide mock modules if hardware-dependent C-extensions or PortAudio are absent
if "sounddevice" not in sys.modules:
    try:
        import sounddevice  # noqa: F401
    except (ImportError, OSError, Exception):
        mock_sd = MagicMock()
        sys.modules["sounddevice"] = mock_sd

if "vosk" not in sys.modules:
    try:
        import vosk  # noqa: F401
    except (ImportError, OSError, Exception):
        mock_vosk = MagicMock()
        sys.modules["vosk"] = mock_vosk
