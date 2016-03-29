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

    def test_minimum_bounding_rectangle(self):
        mbr = utils.minimum_bounding_rectangle(self.points)
        self.assertEqual(mbr, [0, 0, 94, 98])

    def test_mbr_area(self):
        mbr = [0, 0, 94, 98]
        area = utils.mbr_area(mbr)
        self.assertEqual(area, 9212)

class TestPointPattern(unittest.TestCase):
    """
    These are the tests that you got working in assignment 3.
    You should not need to alter these at all.
    """
    @classmethod
    def setUp(self):
        pass

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = utils.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)

    def test_manhattan_distance(self):
        """
        A test to ensure that the distance between points
        is being properly computed.

        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `eucliden_distance` function so that the correct
        values are returned.

        Something to think about: Why might you want to test
        different cases, e.g. all positive integers, positive
        and negative floats, coincident points?
        """
        point_a = (3, 7)
        point_b = (1, 9)
        distance = utils.manhattan_distance(point_a, point_b)
        self.assertEqual(4.0, distance)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = utils.manhattan_distance(point_a, point_b)
        self.assertEqual(10.9, distance)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = utils.manhattan_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_euclidean_distance(self):
        """
        A test to ensure that the distance between points
        is being properly computed.

        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `eucliden_distance` function so that the correct
        values are returned.

        Something to think about: Why might you want to test
        different cases, e.g. all positive integers, positive
        and negative floats, coincident points?
        """
        point_a = (3, 7)
        point_b = (1, 9)
        distance = utils.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(2.8284271, distance, 4)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = utils.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(7.7074639, distance, 4)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = utils.euclidean_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_shift_point(self):
        """
        Test that a point is being properly shifted
         when calling point_pattern.shift_point
        """
        point = (0, 0)
        new_point = utils.shift_point(point, 3, 4)
        self.assertEqual((3, 4), new_point)

        point = (-2.34, 1.19)
        new_point = utils.shift_point(point, 2.34, -1.19)
        self.assertEqual((0, 0), new_point)

    def test_check_coincident(self):
        """
        As above, update the function in point_pattern.py

        """
        point_a = (3, 7)
        point_b = (3, 7)
        coincident = utils.check_coincident(point_a, point_b)
        self.assertEqual(coincident, True)

        point_b = (-3, -7)
        coincident = utils.check_coincident(point_a, point_b)
        self.assertEqual(coincident, False)

        point_a = (0, 0)
        point_b = (0.0, 0.0)
        coincident = utils.check_coincident(point_b, point_a)
        self.assertEqual(coincident, True)

    def test_check_in(self):
        """
        As above, update the function in point_pattern.py
        """
        point_list = [(0, 0), (1, 0.1), (-2.1, 1),
                      (2, 4), (1, 1), (3.5, 2)]

        inlist = utils.check_in((0, 0), point_list)
        self.assertTrue(inlist)

        inlist = utils.check_in((6, 4), point_list)
        self.assertFalse(inlist)
