## 1. Describe the Problem

As a user
So that I can check grammer and return stats
I need to be able to add text, verify it has correct grammer and return the % of checks that have passed the check defined in the 'check' method.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

class GrammarStats:
    def __init__(self):
        pass
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        pass
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass


```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
GrammerStats()
It will take no arguments and will nitialise a GrammarStats object. It will also instantiate 2 global int variables, 1 for number of text checks returning True and 1 for number of test checks returning False
"""
grammer_stats = GrammerStats() => [grammer_stats]

"""
check()
It will take a string and should return a bool of True if grammer is correct, otherwise a bool of False
"""
grammer_stats.check("This is the first entry in the grammer stats check!") => ["First entry: This is the first entry in the diary."]

"""
percentage_good()
It will take no arguments and should return an int which is the percentage of texts checks so far that have passed. It will use the global variables for the calculation
"""
grammer_stats.percentage_good() => [10]

Ensure all test function names are unique, otherwise pytest will ignore them!