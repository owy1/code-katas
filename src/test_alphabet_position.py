"""This module tests alphabet_position.py."""
# import pytest


def test_alphabet_position_0_0():
    """Test alphabet_position with text."""
    from alphabet_position import alphabet_position
    result = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert alphabet_position("The sunset sets at twelve o' clock.") == result


def test_alphabet_position_0_1():
    """Test alphabet_position with text."""
    from alphabet_position import alphabet_position
    result = "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
    assert alphabet_position("The narwhal bacons at midnight.") == result


def test_alphabet_position_0_2():
    """Test alphabet_position with text."""
    from alphabet_position import alphabet_position
    result = "8 5 12 12 15 23 15 18 12 4"
    assert alphabet_position("Hello World!") == result


def test_alphabet_position_0_3():
    """Test alphabet_position with text."""
    from alphabet_position import alphabet_position
    result = "20 8 9 19 9 19 4 9 6 6 9 3 21 12 20"
    assert alphabet_position("this is difficult") == result


def test_alphabet_position_0_4():
    """Test alphabet_position with text."""
    from alphabet_position import alphabet_position
    result = "16 25 20 8 15 14 6 15 18 13 1 20"
    assert alphabet_position("python format") == result


def test_alphabet_position_0_5():
    """Test alphabet_position with text."""
    from alphabet_position import alphabet_position
    result = "8 20 20 16 23 23 23 18 5 4 2 15 24 3 15 13"
    assert alphabet_position("http://www.redbox.com/") == result


"""
print(alphabet_position("The sunset sets at twelve o' clock."))
#"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

print(alphabet_position("The narwhal bacons at midnight."))
#"20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"

print(alphabet_position("Hello World!")) #8 5 12 12 15 23 15 18 12 4
print(alphabet_position("this is difficult")) #20 8 9 19 9 19 4 9 6 6 9 3 21 12 20
print(alphabet_position("python format")) #16 25 20 8 15 14 6 15 18 13 1 20
print(alphabet_position("http://www.redbox.com/"))
#8 20 20 16 23 23 23 18 5 4 2 15 24 3 15 13
"""
