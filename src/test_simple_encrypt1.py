"""This module tests simple_encrypt1.py."""
# import pytest


def test_decrypt_0_0():
    """Test decrypt with encrypt_text, n = 0."""
    from simple_encrypt1 import decrypt
    assert decrypt("This is a test!", 0) == "This is a test!"


def test_decrypt_0_1():
    """Test decrypt with encrypt_text, n = 1."""
    from simple_encrypt1 import decrypt
    assert decrypt("hsi  etTi sats!", 1) == "This is a test!"


def test_decrypt_0_3():
    """Test decrypt with encrypt_text, n = 2."""
    from simple_encrypt1 import decrypt
    assert decrypt("s eT ashi tist!", 2) == "This is a test!"


 def test_encrypt_0_1():
    """Test encrypt with text, n = 0."""
    from simple_encrypt1 import encrypt
    assert encrypt("This is a test!", 0) == "This is a test!"


def test_encrypt_0_2():
    """Test encrypt with text, n = 1."""
    from simple_encrypt1 import encrypt
    assert encrypt("This is a test!",1) == "hsi  etTi sats!"


def test_encrypt_0_3():
    """Test encrypt with text, n = 2."""
    from simple_encrypt1 import encrypt
    assert encrypt("This is a test!",2) == "s eT ashi tist!"


"""
print(encrypt("This is a test!",0)) # "This is a test!"
print(encrypt("This is a test!",1)) # "hsi  etTi sats!"
print(encrypt("This is a test!",2)) # "s eT ashi tist!"
print(decrypt("This is a test!", 0)) # "This is a test!"
print(decrypt("hsi  etTi sats!", 1)) # "This is a test!"
print(decrypt("s eT ashi tist!", 2)) # "This is a test!"
print(encrypt("This is hard!",-1)) # "This is hard!"
print(decrypt("This is hard!",-1)) # "This is hard!"
print(encrypt("This is hard!",1)) # "hsi adTi shr!"
print(decrypt("hsi adTi shr!",1)) # "This is hard!"
"""
