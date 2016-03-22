import math  # I am guessing that you will need to use the math module
import json  # I would like you to use the JSON module for reading geojson (for now)


def read_geojson(input_file):
    """
    Read a geojson file

    Parameters
    ----------
    input_file : str
                 The PATH to the data to be read

    Returns
    -------
    gj : dict
         An in memory version of the geojson
    """
    # Please use the python json module (imported above)
    # to solve this one.
    with open('data/us_cities.geojson') as f:
        gj = json.load(f)
    return gj


def find_largest_city(gj):
    """
    Iterate through a geojson feature collection and
    find the largest city.  Assume that the key
    to access the maximum population is 'pop_max'.

    Parameters
    ----------
    gj : dict
         A GeoJSON file read in as a Python dictionary

    Returns
    -------
    city : str
           The largest city

    population : int
                 The population of the largest city
    """
    max_population = 0
    for feature in gj['features']:
        test_max_population = feature['properties']['pop_max']
        if test_max_population > max_population:
            max_population = test_max_population
            city = feature['properties']['name']


    return city, max_population


def highest_latitude(gj):
    """
    Here you will write your own code to find
    some attribute in the supplied geojson file.

    Take a look at the attributes available and pick
    something interesting that you might like to find
    or summarize.  This is totally up to you.

    Do not forget to write the accompanying test in
    tests.py!
    """
    latHigh=0.0
    for feature in gj['features']:
        latitude = feature['properties']['latitude']
        if latitude>latHigh:
            latHigh=latitude
            city = feature['properties']['name']
    return city, latHigh