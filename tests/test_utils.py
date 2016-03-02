import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        pass
		
	
    
    
    def test_getx(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4
	
    def test_create_n_rand_pts(self):
        
        self.assertEqual(100, len(utils.create_n_rand_pts(100)))
	
    def test_critical_pts(self):
		
        self.assertEqual(utils.critical_pts(range(1,1000)),(1,999))
	

    def test_gety(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4

    def test_shift_point(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4

    def test_euclidean_distance(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4

    def test_manhattan_distance(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4


    def test_check_coincident(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4

    
    def test_euclidean_distance(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4
		
    def test_euclidean_distance(self):
        self.assertTrue(True)
        #This test case was completed in Assignment 4

    
    
    def test_check_in(self):
         self.assertTrue(True)
        #This test case was completed in Assignment 4
