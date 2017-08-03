# -*- coding: utf-8 -*-
"""Tests for string-pyramid.py."""


import pytest


def test_string_pyramid_3_side():
    """Module side pyramid."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('abc') == '  c  \n bbb \naaaaa'


def test_string_pyramid_3_above():
    """Module above pyramid."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('abc') == 'aaaaa\nabbba\nabcba\nabbba\naaaaa'


def test_string_pyramid_3_count_visible():
    """Module count visible characters."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('abc') == 25


def test_string_pyramid_3_count_all():
    """Module count all characters."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('abc') == 35


def test_string_pyramid_2_side():
    """Module side pyramid."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('*#') == ' # \n***'


def test_string_pyramid_2_above():
    """Module above pyramid."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('*#') == '***\n*#*\n***'


def test_string_pyramid_2_count_visible():
    """Module count visible characters."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('*#') == 9


def test_string_pyramid_2_count_all():
    """Module count all characters."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('*#') == 10
