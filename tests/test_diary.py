from lib.diary import *

def test_initialise_diaryentry():
    diary_entry = DiaryEntry("First entry", "This is the first entry in the diary.")

def test_diaryentry_formatted():
    diary_entry = DiaryEntry("First entry", "This is the first entry in the diary.")
    assert diary_entry.format() == "First entry: This is the first entry in the diary."

def test_diaryentry_word_count():
    diary_entry = DiaryEntry("First entry", "This is the first entry in the diary.")
    assert diary_entry.count_words() == 10

def test_diaryentry_return_reading_time():
    diary_entry = DiaryEntry("First entry", "This is the first entry in the diary.")
    assert diary_entry.reading_time(2) == 5

def test_diaryentry_return_reading_chunk():
    diary_entry = DiaryEntry("First entry", "This is the first entry in the diary.")
    assert diary_entry.reading_chunk(2, 2) == "First entry This is"
    assert diary_entry.reading_chunk(2, 3) == "the first entry in the diary."