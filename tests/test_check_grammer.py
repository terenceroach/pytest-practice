import pytest
from lib.check_grammer import *

def test_check_grammer_begins_uppercase_true():
    result = check_grammer("Hello, and welcome to my program!")
    assert result == True

def test_check_grammer_ends_with_suitable_char_true():
    result = check_grammer("Hello, and welcome to my program!")
    assert result == True

def test_check_grammer_begins_uppercsae_false():
    result = check_grammer("hello, and welcome to my program!")
    assert result == False

def test_check_grammer_ends_with_suitable_char_false():
    result = check_grammer("Hello, and welcome to my program")
    assert result == False 

def test_check_grammer_non_string_value():
    with pytest.raises(Exception) as e:
        check_grammer(24)
    error_message = str(e.value)
    assert error_message == "You must provide a string"