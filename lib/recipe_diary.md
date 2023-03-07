## 1. Describe the Problem

As a user
So that I can maintain a diary
I need to be able to add a diary entry and return chunks to read based on time available.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        pass

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        pass

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass


```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Initialise a DiaryEntry
It should initialise correctly
"""
diary_entry = DiaryEntry("First Entry", "This is the first entry in the diary.") => [title = "First entry", contents = "First entry: This is the first entry in the diary."]

"""
Check diary format
It should return a string of the diary entry correctly formatted
"""
diary_entry.format("First Entry", "This is the first entry in the diary.") => ["First entry: This is the first entry in the diary."]

"""
Count words
It should return an int which is the number of words in the diary
"""
diary_entry.count_words("First Entry", "This is the first entry in the diary.") => [10]

"""
Check reading time
It should return an int which is the estimated reading time in minutes based on the words per minute
"""
diary_entry.reading_time("First Entry", "This is the first entry in the diary.") => [5]

"""
Check reading chunk
It should return a chunk of text that can be read based on words per minute
"""
diary_entry.reading_chunk()"First Entry", "This is the first entry in the diary.") => ["First entry: This is the"]

"""
Check second reading chunk
It should return a futher chunk of text that can be read based on words per minute when called again
"""
diary_entry.reading_chunk("First Entry", "This is the first entry in the diary.") => ["first entry in the diary."]


Ensure all test function names are unique, otherwise pytest will ignore them!