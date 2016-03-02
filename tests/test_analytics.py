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
  	pass

  def test_permutations(self):
    self.assertEqual(len(analytics.permutations(100)), 100)
