import os
import sys
import unittest
import numpy
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

  def setUp(self):
    pass


  def test_compute_critical(self):
    self.assertTrue(self.lower > .01)
    self.assertTrue(self.upper < .10)

  def test_permutations(self):
    point_count = 9
    self.assertEqual(point_count, analytics.permutations(point_count))
