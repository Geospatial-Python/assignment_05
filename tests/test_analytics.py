import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        cls.points = [(random.uniform(0,1), random.uniform(0,1)) for i in range(50)]

    def test_permutation(self):
        list = analytics.permutation_nearest_distance()
        self.assertEqual(99,len(list))
        list = analytics.permutation_nearest_distance(50,20)
        self.assertEqual(50,len(list))

    def test_critical(self):
        list = analytics.permutation_nearest_distance()
        critical = analytics.critical_points(list)
        self.assertEqual(min(list),critical[0])
        self.assertEqual(max(list),critical[1])

    def test_significant(self):
        critical = analytics.critical_points(analytics.permutation_nearest_distance())

        distance = random.uniform(0,critical[0]-.000000001) #distance < min +
        self.assertTrue(analytics.significant(critical,distance))

        distance = random.uniform(critical[1]+.00000000000000001,9999999999999999999999999999999999999999999999999999999999) #distance > max
        self.assertTrue(analytics.significant(critical,distance))

        distance = random.uniform(critical[0],critical[1]) # min < distance < max
        self.assertFalse(analytics.significant(critical,distance))

    def test_average_nearest_neighbor_distance(self):
        mean_d = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(mean_d, 0.0884470472, 5)
    """
    Changed from 7.629178 to 0.0884470472 because with the changed domain from (1-100) to (0-1), mean_d will be very different
    """

    def test_mean_center(self):
        """
        Something to think about - What values would you
         expect to see here and why?  Why are the values
         not what you might expect?
        """
        """
        Changed assert statements/test values slightly to match with domain of [0,1]
        """

        x, y = analytics.mean_center(self.points)
        self.assertAlmostEqual(x, 0.50273194,5)
        self.assertAlmostEqual(y, 0.45796236, 5)

    def test_minimum_bounding_rectangle(self):
        mbr = analytics.minimum_bounding_rectangle(self.points)
        self.assertAlmostEqual(mbr[0], 0.003331,5)
        self.assertAlmostEqual(mbr[1], 0.003184,5)
        self.assertAlmostEqual(mbr[2], 0.994604,5)
        self.assertAlmostEqual(mbr[3], 0.967482,5)

    def test_mbr_area(self):
        mbr = [0,0,94,98]
        area = analytics.mbr_area(mbr)
        self.assertEqual(area, 9212)

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = analytics.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)


