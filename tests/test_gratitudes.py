from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("beer")
    # gratitudes.format()
    assert gratitudes.format() == "Be grateful for: beer"