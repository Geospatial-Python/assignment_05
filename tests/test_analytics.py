import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics


class TestAnalytics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        random.seed(12345)
        cls.points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(50)]

    """

    Tests don't seem to work because of import issue with us_cities.

    def test_find_largest(self):
        city, pop = analytics.find_largest_city(self.gj)
        self.assertEqual(city, 'New York')
        self.assertEqual(pop, 19040000)

    also write_your_own

    """

    def test_mean_center(self):
        x, y = analytics.mean_center(self.points)
        self.assertAlmostEqual(x, 47.52)
        self.assertAlmostEqual(y, 45.14)

    def test_average_nearest_neighbor_distance(self):
        mean_d = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(mean_d, 7.629178, 5)

    def test_minimum_bounding_rectangle(self):
        mbr = analytics.minimum_bounding_rectangle(self.points)
        self.assertEqual(mbr, [0, 0, 94, 98])

    def test_mbr_area(self):
        mbr = [0, 0, 94, 98]
        area = analytics.mbr_area(mbr)
        self.assertEqual(area, 9212)