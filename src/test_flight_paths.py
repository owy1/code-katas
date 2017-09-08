#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for flight_paths.py."""


import pytest


CITIES = [
    ('San Diego', 'Seattle', "path: ['San Diego', 'Sacramento', 'Seattle'], total distance: 1085.98 miles."),
    ('Seattle', 'London', "path: ['Seattle', 'London'], total distance: 4781.51 miles."),
    ('New York City', 'London', "path: ['New York City', 'Boston', 'London'], total distance: 3459.63 miles.")
]


@pytest.mark.parametrize('city1, city2, result', CITIES)
def test_flight_paths(city1, city2, result):
    """Test flight paths between cities."""
    from flight_paths import find_shortest_flight_paths
    assert find_shortest_flight_paths(city1, city2)
