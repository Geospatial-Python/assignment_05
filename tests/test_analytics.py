import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        vals = [1,2,3,4,5,6,7,8,9]
        self.lower, self.upper = analytics.compute_critical(vals)

    def test_compute_critical(self):
        self.assertTrue(self.lower == 1 and self.upper == 9)

    def test_check_significant(self):
        significant = [analytics.check_significant(self.lower, self.upper, 9.01),
                       analytics.check_significant(self.lower, self.upper, 7.77)]
        self.assertTrue(significant[0])
        self.assertFalse(significant[1])
