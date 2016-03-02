import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
       self.rand_points = utils.create_random(100)
       self.permutations = utils.permutations(99)

     def test_create_random(self):
     self.assertEqual(100, len(self.rand_points))

     def test_permutations(self):
         self.assertEqual(len(self.permutations), 99)
         self.assertNotEqual(self.permutations[0], self.permutations[1])
