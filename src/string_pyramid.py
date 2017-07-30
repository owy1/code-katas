"""This module builds a pyramid from charactes from a given string."""

# -*- coding: utf-8 -*-


def watch_pyramid_from_the_side(characters):
    """Show pyramid side-view."""
    if not characters: return characters
    reverse_characters = characters[::-1]
    n = len(characters)
    space = 2 * n - 2
    matrix = ""
    for idx, item in enumerate(reverse_characters):
        for j in range(space - 1):
            matrix += ""
        space = space - 1
        for j in range(2 * idx + 1):
            matrix += item
        for j in range(space - 1):
            matrix += " "
        matrix += "\n"
    return matrix[:-1]


def watch_pyramid_from_above(characters):
    """Show pyramid top-view."""
    if not characters: return characters
    reverse_str = (characters[::-1])[1:]
    n = len(characters)
    head = ""
    tail = ""
    matrix = ""
    k = 2 * n - 2
    for idx, item in enumerate(characters):
        matrix += head
        for j in range(k + 1):
            matrix += item
        matrix += tail
        matrix += "\n"
        head = head + item
        tail = item + tail
        k = k - 2
    head = characters[:-1]
    tail = reverse_str
    k = 1
    for idx, item in enumerate(reverse_str):
        matrix += head
        for j in range(k):
            matrix += item
        matrix += tail
        matrix += "\n"
        head = head[:-1]
        tail = tail[1:]
        k = k + 2
    return matrix[:-1]


def count_visible_characters_of_the_pyramid(characters):
    """Return count of visible characters to outside."""
    if not characters: return -1
    return (2 * len(characters) - 1) ** 2


def count_all_characters_of_the_pyramid(characters):
    """Return all characters of pyramid."""
    if not characters: return -1
    n = len(characters)
    tot = 0
    for i in range(n, 0, -1):
        tot += (2 * n - 1) ** 2
        n -= 1
    return tot
