from lib.check_codeword import *

def test_check_codeeord_return_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_return_close():
    result = check_codeword("here")
    assert result == "Close, but nope."

def test_check_codeword_return_wrong():
    result = check_codeword("terry")
    assert result == "WRONG!"