import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):

        random_points = analytics.create_random(100)
        self.assertEqual(100, len(random_points))

        permutations = analytics.permutations(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = analytics.compute_critical(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

        # As above, update the module and function name.
        significant = analytics.check_significant(lower, upper, observed_avg)
        self.assertTrue(significant)

        pass
