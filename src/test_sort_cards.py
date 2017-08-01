# -*- coding: utf-8 -*-
"""Tests for sort_cards.py."""


import pytest

INSERT_TABLE = [
    (['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    (['Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    (['5', '4', 'T', 'Q', 'K', 'J', '6', '9', '3', '2', '7', 'A', '8'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'])
]


@pytest.mark.parametrize('values, sorted', INSERT_TABLE)
def test_init_with_iterable(values, sorted):
    """."""
    from sort_cards import sort_cards
    assert sort_cards(values) == sorted
