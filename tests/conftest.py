import sys
from unittest.mock import MagicMock

# Gracefully provide mock modules if hardware-dependent C-extensions are absent
if "sounddevice" not in sys.modules:
    try:
        import sounddevice  # noqa: F401
    except ImportError:
        mock_sd = MagicMock()
        sys.modules["sounddevice"] = mock_sd

if "vosk" not in sys.modules:
    try:
        import vosk  # noqa: F401
    except ImportError:
        mock_vosk = MagicMock()
        sys.modules["vosk"] = mock_vosk

