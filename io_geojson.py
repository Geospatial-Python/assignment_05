import json


def read_geojson(input_file):
    with open(input_file) as f:
        gj = json.load(f)
    return gj

    """I got the import working by eliminating the ..
    and placing the data folder inside assignment_05

    print(read_geojson('data/us_cities.geojson'))

    """
