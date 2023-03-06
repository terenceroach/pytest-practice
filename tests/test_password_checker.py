import pytest
from lib.password_checker import *


def test_password_equals_8():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check("12345678") == True

def test_password_exception():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check("123")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."