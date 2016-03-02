import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_permutations(self):
        self.assertEqual(len(analytics.permutations(100)), 100)
        
    def test_critical(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(min(list), 1)
        self.assertEqual(max(list), 5)
    
    def test_significance(self):
        self.assertTrue(analytics.significant_distance(1, 6, 7))
        self.assertTrue(analytics.significant_distance(2, 8, 1))
        self.assertFalse(analytics.significant_distance(2, 8, 5))
