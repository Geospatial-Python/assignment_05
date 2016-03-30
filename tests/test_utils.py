import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import utils
import analytics


class TestUtils(unittest.TestCase):

    def setUp(self):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        self.points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(50)]

    def test_getx(self):
        point = (1, 2)
        x = utils.getx(point)
        self.assertEqual(1, x)

    def test_gety(self):
        point = (3, 2.5)
        y = utils.gety(point)
        self.assertEqual(2.5, y)

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = utils.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)

    def test_manhattan_distance(self):
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
        point = (0, 0)
        new_point = utils.shift_point(point, 3, 4)
        self.assertEqual((3, 4), new_point)

        point = (-2.34, 1.19)
        new_point = utils.shift_point(point, 2.34, -1.19)
        self.assertEqual((0, 0), new_point)

    def test_check_coincident(self):
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
        point_list = [(0, 0), (1, 0.1), (-2.1, 1),
                      (2, 4), (1, 1), (3.5, 2)]

        inlist = utils.check_in((0, 0), point_list)
        self.assertTrue(inlist)

        inlist = utils.check_in((6, 4), point_list)
        self.assertFalse(inlist)

    def test_generate_random_points(self):
        rand_points = utils.generate_random_points(100)
        self.assertEqual(100, len(rand_points))

    def test_permutations(self):
        permutations = utils.permutations(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

    def test_crit_tations(self):
        observed_avg = analytics.average_nearest_neighbor_distance(self.points)
        permutations = utils.permutations(99)
        lower, upper = utils.crit_tations(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

    def test_check_yer_sig(self):
        permutations = utils.permutations(99)
        lower, upper = utils.crit_tations(permutations)
        significant = utils.check_yer_sig(lower, upper, observed)
        self.assertTrue(significant)
