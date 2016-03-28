import json


def read_geojson(input_file):

    with open(input_file, 'r') as f:
        gj = json.load(f)

    return gj


def find_largest_city(gj):

    city = None
    max_population = 0

    for i in gj['features']:
        if i['properties']['pop_max'] > max_population:
            max_population = i['properties']['pop_max']
            city = i['properties']['name']

    return city, max_population


