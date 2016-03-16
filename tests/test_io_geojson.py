import unittest
import io_geojson


class TestIoGeoJson(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.gj = io_geojson.read_geojson('data/us_cities.geojson')

    def read_geojson(self):
        self.assertIsInstance(self.gj, dict)

