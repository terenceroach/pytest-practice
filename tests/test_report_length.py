from lib.report_length import report_length

def test_report_length_returns_for_five():
    result = report_length("Terry")
    assert result == "This string was 5 characters long"

def test_report_length_returns_for_eight():
    result = report_length("bootcamp")
    assert result == "This string was 8 characters long"