import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics
from .. import utils
#import analytics
#import utils
import random

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        i = 0
        self.points = []
        while i < 100:
            seed = (round(random.random(),2), round(random.random(),2))
            self.points.append(seed)
            n_additional = random.randint(5,10)
            i += 1
            c = random.choice([0,1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt = (round(seed[0] + x_offset, 2), round(seed[1] + y_offset,2))
                    self.points.append(pt)
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break

        random.seed()  # Reset the random number generator using system time
        self.observed_avg = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(0.027, self.observed_avg, 3)

        permutations = utils.permutations(99)
        self.lower, self.upper = analytics.compute_critical(permutations)

    def test_compute_critical(self):
        self.assertTrue(self.lower > 0.03)
        self.assertTrue(self.upper < 0.07)
        self.assertTrue(self.observed_avg < self.lower or self.observed_avg > self.upper)

    def test_check_significant(self):
        significant = analytics.check_significant(self.lower, self.upper, 101)
        self.assertTrue(significant)
