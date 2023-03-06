from lib.string_builder import *

def test_string_builder_returns_size_and_string():
    string_builder = StringBuilder()
    string_builder.add("Terry")
    assert string_builder.size() == 5
    assert string_builder.output() == "Terry"