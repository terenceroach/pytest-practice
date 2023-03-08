from lib.grammer_stats import *

# suite of unit test for check method
def test_check_returns_true_if_both_conditions_good():
    grammer_stats = GrammerStats()
    text = "This is the first entry in the grammer stats check!"
    assert grammer_stats.check(text) == True

def test_check_returns_false_if_not_start_with_capital_letter():
    grammer_stats = GrammerStats()
    text = "this is the first entry in the grammer stats check!"
    assert grammer_stats.check(text) == False

def test_check_returns_false_if_not_end_with_valid_char():
    grammer_stats = GrammerStats()
    text = "This is the first entry in the grammer stats check"
    assert grammer_stats.check(text) == False

# Suite of unit test for pecentage_good method
def test_percentage_good_returns_int_100_as_percentage():
    grammer_stats = GrammerStats()
    text = "This is the first entry in the grammer stats check!"
    grammer_stats.check(text)
    assert grammer_stats.percentage_good() == 100

def test_percentage_good_returns_int_50_as_percentage():
    grammer_stats = GrammerStats()
    text = "This is the first entry in the grammer stats check!"
    text2 = "this is the second entry in the grammer stats check!"
    grammer_stats.check(text)
    grammer_stats.check(text2)
    assert grammer_stats.percentage_good() == 50

def test_percentage_good_returns_int_33_as_percentage():
    grammer_stats = GrammerStats()
    text = "This is the first entry in the grammer stats check!"
    text2 = "this is the second entry in the grammer stats check!"
    text3 = "This is the third entry in the grammer stats check!"
    grammer_stats.check(text)
    grammer_stats.check(text2)
    grammer_stats.check(text3)
    assert grammer_stats.percentage_good() == 66
