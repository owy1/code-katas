"""This module find a path between two cities and return total distance."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import os
import json
from shortpath import Graphplus, dijkstrategy


__location__ = os.path.join(os.path.dirname(__file__), 'cities_with_airports.json')


def calculate_distance(point1, point2): # pragma: no cover
    """
    Calculate distance (miles) between point1 and point2 [latitude, longitude].
    Return value is float.
    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html.
    """
    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(radius_earth * c / 1.60934, 2)  # convert km to miles


def load_json_data(): # pragma: no cover
    """Open json file."""
    with open(__location__, 'r') as f:
        content = json.load(f)
    return content


def parse_json_data(): # pragma: no cover
    """Parse json data."""
    data = load_json_data()
    dic = {}
    for city in data:
        dic[city['city']] = {
            "lat_lon": city["lat_lon"],
            "neighbors": city["destination_cities"]}
    return dic


def dic_to_weigh_graphs(): # pragma: no cover
    """."""
    city_airports = parse_json_data()
    airport_graphs = Graphplus()
    for city, city_data in city_airports.items():
        city_airport = city
        city_neighbors = city_data['neighbors']
        for neighbor in city_neighbors:
            try:
                dist_between_airports = calculate_distance(city_data['lat_lon'], city_airports[neighbor]['lat_lon'])
            except KeyError:
                continue
            airport_graphs.add_edge(city_airport, neighbor, dist_between_airports)
    return airport_graphs


def find_shortest_flight_paths(city1, city2):
    """."""
    g = dic_to_weigh_graphs()
    if city1 not in g.nodes() or city2 not in g.nodes():
        raise KeyError('invalid city name')
    try:
        res = dijkstrategy(g, city1, city2)
        return "path: {}, total distance: {} miles.".format(res[0], res[1])
    except KeyError:
        print("No flight path between {} and {}.".format(city1, city2))

if __name__ == '__main__':  # pragma: no cover
    city1 = 'San Diego'
    city2 = 'Seattle'
    city3 = 'London'
    city4 = 'New York City'
    print(find_shortest_flight_paths(city4, city3))
