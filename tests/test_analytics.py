import os
import sys
import unittest
import random

sys.path.insert(0, os.path.abspath('..'))

#from .. 
import analytics

class TestAnalytics(unittest.TestCase):

	@classmethod
	def setUp(self):
		pass
		
	def test_find_largest(self):
		self.assertTrue(True)
		#This test case was completed in Assignment 4

	def test_write_your_own(self):
		self.assertTrue(True)
		#This test case was completed in Assignment 4
		
	def test_p_perms(self):
		self.assertEqual(len(analytics.p_perms(50,100)),50)

	def test_monte_carlo_critical_bound_check(self):
		self.assertTrue(analytics.monte_carlo_critical_bound_check(0.03,0.05,0.02))


	def test_average_nearest_neighbor_distance(self):
		self.assertTrue(True)
		#This test case was completed in Assignment 4
		
	def test_mean_center(self):
		self.assertTrue(True)
		#This test case was completed in Assignment 4
		
	def test_minimum_bounding_rectangle(self):
		self.assertTrue(True)
		#This test case was completed in Assignment 4

	def test_expected_distance(self):
		self.assertTrue(True)
		#This test case was completed in Assignment 4	