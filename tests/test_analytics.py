import os
import sys
import unittest

from numpy.core.defchararray import upper, lower

sys.path.insert(0, os.path.abspath('..'))

from .. import analytics


class TestAnalytics(unittest.TestCase):

    def setUp(self):
        pass

    def test_compute_critical(self):
        self.assertTrue(lower == 1)
        self.assertTrue(upper == 0)

    def test_check_significant(self):

        significant = [analytics.check_significant(self.lower, self.upper, 3)]

        self.assertTrue(significant[0])
        self.assertFalse(significant[1])
