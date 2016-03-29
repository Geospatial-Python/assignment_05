import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gj = point_pattern.read_geojson('..data/us_cities.geojson')

    def test_read_geojson(self):
        self.assertIsInstance(self.gj, dict)

    def test_find_largest(self):
        city, pop = point_pattern.find_largest_city(self.gj)
        self.assertEqual(city, 'New York')
        self.assertEqual(pop, 19040000)