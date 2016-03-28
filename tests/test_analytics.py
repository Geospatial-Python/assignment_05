import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

from .. import analytics


class TestAnalytics(unittest.TestCase):

    def setUp(self):

        pass

    def test_compute_critical(self):

        self.assertTrue(self.l == 0)
        self.assertTrue(self.u == 9)

    def test_check_significant(self):

        significant = [analytics.check_significant(self.l, self.u, self.observed)]

        self.assertTrue(significant[0])
        self.assertFalse(significant[1])
