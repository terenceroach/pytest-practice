from lib.word_count import *

def test_return_number_of_words_in_string():
    word_count = count_words("Hello this is Terry")
    assert word_count == 4