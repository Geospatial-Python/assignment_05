import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import io_geojson

class TestIoGeoJson(unittest.TestCase):

    @classmethod
    def setUp(self):
        pass