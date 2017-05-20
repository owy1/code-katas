"""Kata6: Replace with Alphabet position.

Given a string, replace every letter with its position in the alphabet.
If anything in text not a letter, ignore it.

#1 Best Practice
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

"""


def alphabet_position(text):
    """Replace alphabets with number."""
    text = ''.join([i for i in text if i.isalpha()])
    text = ' '.join(str(ord(x) - 96) for x in text.lower())
    return text
