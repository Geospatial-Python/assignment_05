import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import io_geojson as point_pattern

class TestIoGeoJson(unittest.TestCase):

	def setUp(self):
		self.gj = point_pattern.read_geojson('data/us_cities.geojson')
		pass

	def test_read_geojson(self):
		self.assertIsInstance(self.gj, dict)

    