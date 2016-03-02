import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics
#------------------------------------------------------------------
#
# Joseph Cruz
# test_analytics.py
#
# Performs tests on the file: analytics.py
#------------------------------------------------------------------
class TestAnalytics(unittest.TestCase):

    def setUp(cls):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        cls.points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function test_mean_nearest_neighbors_randomPoints()
#
# Tests that the function generates a set of means of random points
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_mean_nearest_neighbors_randomPoints(self):
        random.seed(12345)
        means_rand = analytics.mean_nearest_neighbors_randomPoints()
        len_rand = len(means_rand)
        self.assertEqual(99,len_rand)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function test_find_crit_points()
#
# Tests that the function generates critical points
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_find_crit_points(self):
        min_max = (0.045735045024117245, 0.057660631669905316)
        random.seed(12345)
        rand_nums_generated = analytics.find_crit_points(analytics.mean_nearest_neighbors_randomPoints())
        self.assertEqual(min_max, rand_nums_generated)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function test_crit_point_check()
#
# Tests that the function properly checks the values of crit points
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_crit_point_check(self):
        min_mean = 0.045735045024117245
        max_mean = 0.057660631669905316
        check_val = analytics.crit_point_check(min_mean,max_mean,1)
        check_val2 = analytics.crit_point_check(min_mean,max_mean,.048)
        self.assertTrue(check_val)
        self.assertFalse(check_val2)

    def test_average_nearest_neighbor_distance(self):
        mean_d = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(mean_d, 7.629178, 5)

    def test_mean_center(self):
        """
        Something to think about - What values would you
         expect to see here and why?  Why are the values
         not what you might expect?
        """
        x, y = analytics.mean_center(self.points)
        self.assertEqual(x, 47.52)
        self.assertEqual(y, 45.14)

    def test_minimum_bounding_rectangle(self):
        mbr = analytics.minimum_bounding_rectangle(self.points)
        self.assertEqual(mbr, [0,0,94,98])

    def test_mbr_area(self):
        mbr = [0,0,94,98]
        area = analytics.mbr_area(mbr)
        self.assertEqual(area, 9212)

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = analytics.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)

class TestOtherAnalytics(unittest.TestCase):

    def setUp(self):
        pass

    def test_euclidean_distance(self):
        """
        A test to ensure that the distance between points
        is being properly computed.

        You do not need to make any changes to this test,
        instead, in analytics.py, you must complete the
        `eucliden_distance` function so that the correct
        values are returned.

        Something to think about: Why might you want to test
        different cases, e.g. all positive integers, positive
        and negative floats, coincident points?
        """
        point_a = (3, 7)
        point_b = (1, 9)
        distance = analytics.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(2.8284271, distance, 4)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = analytics.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(7.7074639, distance, 4)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = analytics.euclidean_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_manhattan_distance(self):
        """
        A test to ensure that the distance between points
        is being properly computed.

        You do not need to make any changes to this test,
        instead, in analytics.py, you must complete the
        `eucliden_distance` function so that the correct
        values are returned.

        Something to think about: Why might you want to test
        different cases, e.g. all positive integers, positive
        and negative floats, coincident points?
        """
        point_a = (3, 7)
        point_b = (1, 9)
        distance = analytics.manhattan_distance(point_a, point_b)
        self.assertEqual(4.0, distance)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = analytics.manhattan_distance(point_a, point_b)
        self.assertEqual(10.9, distance)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = analytics.manhattan_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_check_coincident(self):
        """
        As above, update the function in analytics.py

        """
        point_a = (3, 7)
        point_b = (3, 7)
        coincident = analytics.check_coincident(point_a, point_b)
        self.assertEqual(coincident, True)

        point_b = (-3, -7)
        coincident = analytics.check_coincident(point_a, point_b)
        self.assertEqual(coincident, False)

        point_a = (0, 0)
        point_b = (0.0, 0.0)
        coincident = analytics.check_coincident(point_b, point_a)
        self.assertEqual(coincident, True)

    def test_check_in(self):
        """
        As above, update the function in analytics.py
        """
        point_list = [(0,0), (1,0.1), (-2.1, 1),
                      (2,4), (1,1), (3.5, 2)]

        inlist = analytics.check_in((0,0), point_list)
        self.assertTrue(inlist)

        inlist = analytics.check_in((6,4), point_list)
        self.assertFalse(inlist)
    
