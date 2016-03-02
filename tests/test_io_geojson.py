import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import io_geojson

class TestIoGeoJson(unittest.TestCase):
    """
    This set of tests is focused on reading some geojson
    data in as a Python dictionary and then answering
    some questions about the data.
    """

    @classmethod
    def setUpClass(cls):
        cls.gj = io_geojson.read_geojson('data/us_cities.geojson')

    def test_read_geojson(self):
        self.assertIsInstance(self.gj, dict)

    def test_find_largest(self):
        city, pop = io_geojson.find_largest_city(self.gj)
        self.assertEqual(city, 'New York')
        self.assertEqual(pop, 19040000)

    def test_write_your_own(self):
        """
        Here you will write a test for the code you write in
        io_geojson.py.
        """
        worldCities = io_geojson.write_your_own(self.gj)
        self.assertEqual(worldCities, 8)
