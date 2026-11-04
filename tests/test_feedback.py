from src.feedback import report_result


def test_report_result_success(capsys):
    report_result(True, "Command executed")
    captured = capsys.readouterr()
    assert captured.out.strip() == "SUCCESS: Command executed"


def test_report_result_failure(capsys):
    report_result(False, "Audio device error")
    captured = capsys.readouterr()
    assert captured.out.strip() == "ERROR: Audio device error"

