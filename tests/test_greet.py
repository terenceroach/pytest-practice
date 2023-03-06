from lib.greet import greet

def test_greet_returns_with_name():
     result = greet("Terry")
     assert result == "Hello, Terry!"