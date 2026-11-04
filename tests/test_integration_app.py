from unittest.mock import MagicMock, patch

from src.integration_app import main


def test_main_missing_files(tmp_path, capsys):
    missing = tmp_path / "song.mp3"
    with patch("sys.argv", ["integration_app.py", str(missing)]):
        ret = main()
        assert ret == 1
        captured = capsys.readouterr()
        assert "ERROR: These media files do not exist" in captured.out


def test_main_vlc_unavailable(tmp_path, capsys):
    song = tmp_path / "song.mp3"
    song.write_text("dummy")

    with patch("sys.argv", ["integration_app.py", str(song)]), \
         patch("src.integration_app.MediaController") as mock_ctrl_cls:
        mock_ctrl = MagicMock()
        mock_ctrl.vlc_available = False
        mock_ctrl_cls.return_value = mock_ctrl

        ret = main()
        assert ret == 1
        captured = capsys.readouterr()
        assert "ERROR: VLC could not be initialized" in captured.out


def test_main_speech_init_failure(tmp_path, capsys):
    song = tmp_path / "song.mp3"
    song.write_text("dummy")

    with patch("sys.argv", ["integration_app.py", str(song)]), \
         patch("src.integration_app.MediaController") as mock_ctrl_cls, \
         patch("src.integration_app.SpeechInput", side_effect=FileNotFoundError("Model missing")):
        mock_ctrl = MagicMock()
        mock_ctrl.vlc_available = True
        mock_ctrl_cls.return_value = mock_ctrl

        ret = main()
        assert ret == 1
        captured = capsys.readouterr()
        assert "ERROR: Could not initialize speech input" in captured.out


def test_main_loop_execution_and_keyboard_interrupt(tmp_path, capsys):
    song = tmp_path / "song.mp3"
    song.write_text("dummy")

    with patch("sys.argv", ["integration_app.py", str(song)]), \
         patch("src.integration_app.MediaController") as mock_ctrl_cls, \
         patch("src.integration_app.SpeechInput") as mock_speech_cls:

        mock_ctrl = MagicMock()
        mock_ctrl.vlc_available = True
        mock_ctrl.execute.return_value = {"success": True, "status": "Stopped"}
        mock_ctrl_cls.return_value = mock_ctrl

        mock_speech = MagicMock()
        mock_speech.listen_and_transcribe.side_effect = [
            OSError("Audio buffer overrun"),
            {"text": "", "confidence": None},
            {"text": "invalid nonsense command", "confidence": 0.8},
            {"text": "play", "confidence": 0.95},
            KeyboardInterrupt(),
        ]
        mock_speech_cls.return_value = mock_speech

        ret = main()
        assert ret == 0
        captured = capsys.readouterr()
        assert "ERROR: Microphone input failed" in captured.out
        assert "REJECTED: No speech recognized" in captured.out
        assert "REJECTED" in captured.out
        assert "SUCCESS: Playback started" in captured.out or "SUCCESS" in captured.out
        assert "Voice assistant stopped" in captured.out
        mock_ctrl.execute.assert_called_with("STOP")

