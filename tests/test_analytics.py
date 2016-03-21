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

        self.assertTrue(self.lower == 0)
        self.assertTrue(self.upper == 9)

    def test_check_significant(self):

        significant = [analytics.check_significant(self.lower, self.upper, self.observed)]

        self.assertTrue(significant[0])
        self.assertFalse(significant[1])
