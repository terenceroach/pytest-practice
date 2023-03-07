# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammer_correct(text):
    """Checks that the text starts with an uppercase character

    Parameters: 
        text: a string containg some text (e.g "Hello and welcome to my program!")
        
    Returns: (state the return value and its type)
        a boolean, True if the text begins with an uppercase character, False if it does not begin
        with an uppercase character

    Side effects: (state any side effects)
        It will raise an ecxeption if anything other than a string paramter is passed.
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text which begins with an uppercase character
It return the boolean True
"""
check_grammer_correct("Hello, and welcome to my program!") => [True]

"""
Given a text which ends with a suitable ending punctuation mark
It returns the boolean True
"""
check_grammer_correct("Hello, and welcome to my program!") => [True]

"""
Given a text which begins with a lowercase character
It returns the boolean False
"""
check_grammer_correct("hello, and welcome to my program!") => [False]

"""
Given a text which doesn't end with a suitable ending punctuation mark
It returns the boolean False
"""
check_grammer_correct("Hello, and welcome to my program") => [False]

"""
Given a date type other than a string
It raises an exception
"""
check_grammer_correct(24) => ["You must provide a string value"]

"""

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!
