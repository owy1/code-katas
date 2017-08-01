"""Kata6: Simple Encryption1, alternating split.

Take every 2nd char from the string, then the other chars,
that are not every 2nd char, and concat them as new String n times.

#1 Best Practice
def decrypt(encrypted_text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text


def encrypt(text,n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

"""


import math


def decrypt(encrypt_text, n):
    """Simple encryption."""
    if not encrypt_text or n <= 0:
        return encrypt_text
    txt_length = len(encrypt_text)
    m = math.floor(txt_length / 2)
    for i in range(n):
        a, b = encrypt_text[m:], encrypt_text[:m]
        encrypt_text = ''.join(x + y for x, y in zip(*(s + s[-1] * (max(len(a), len(b)) - len(s)) for s in (a, b))))
        if txt_length % 2 != 0:
            encrypt_text = encrypt_text[:-1]
    return encrypt_text


def encrypt(text, n):
    """Simple decryption."""
    if not text or n <= 0: return text
    for i in range(n):
        evn_char = text[1::2]
        odd_char = text[::2]
        text = evn_char + odd_char
    return text
