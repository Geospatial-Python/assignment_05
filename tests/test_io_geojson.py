import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import io_geojson
#import io_geojson
import json

class TestIoGeoJson(unittest.TestCase):

    def setUp(self):
        #self.filePath = 'data/us_cities.geojson'
        self.filePath = 'us_cities.geojson'
        with open(self.filePath,'r') as f:
            self.gjfile = json.load(f)

    def test_read_geojson(self):
        _gj = io_geojson.read_geojson(self.filePath)
        self.assertEqual(self.gjfile, _gj)
