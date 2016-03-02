import os
import sys
import unittest
import random

sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

	@classmethod
    def setUp(self):
        pass
		
	def test_find_largest(self):
        city, pop = analytics.find_largest_city(self.gj)
        self.assertEqual(city, 'New York')
        self.assertEqual(pop, 19040000)

	def test_write_your_own(self):
        """
        Here you will write a test for the code you write in
        analytics.py.
        """
        some_return = analytics.write_your_own(self.gj)
        self.assertEqual(187,some_return)
		
	def test_p_perms(self):
		self.assertEqual(len(analytics.p_perms()),99)

	def test_monte_carlo_critical_bound_check(self):
		self.assertTrue(0.03,0.05,0.02)


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

	def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = analytics.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)		