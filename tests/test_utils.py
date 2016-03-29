import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        cls.points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(50)]

    def test_average_nearest_neighbor_distance(self):
        mean_d = utils.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(mean_d, 7.629178, 5)

    def test_mean_center(self):
        """
        Something to think about - What values would you
         expect to see here and why?  Why are the values
         not what you might expect?
        """
        x, y = utils.mean_center(self.points)
        self.assertAlmostEqual(x, 47.52)
        self.assertAlmostEqual(y, 45.14)
