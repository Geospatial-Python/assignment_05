import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):

    def setUp(cls):
        random.seed(12345)
        cls.points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# function test_generate_rand_points()
#
# Tests that the function generates an integer number of random
# points based on user input Points will be within the domain [0,1]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def test_generate_rand_points(self):
        random.seed(12345)
        listOfPoints = utils.generate_rand_points(5)
        checkPoints = [(0.41661987254534116, 0.010169169457068361), (0.8252065092537432, 0.2986398551995928), (0.3684116894884757, 0.19366134904507426), (0.5660081687288613, 0.1616878239293682), (0.12426688428353017, 0.4329362680099159)]
        self.assertEqual(listOfPoints,checkPoints)

    def test_getx(self):
        """
        A simple test to ensure that you understand how to access
        the x coordinate in a tuple of coordinates.

        You do not need to make any changes to this test,
        instead, in utils.py, you must complete the
        `getx` function so that the correct
        values are returned.
        """
        point = (1,2)
        x = utils.getx(point)
        self.assertEqual(1, x)

    def test_gety(self):
        """
        As above, except get the y coordinate.

        You do not need to make any changes to this test,
        instead, in utils.py, you must complete the
        `gety` function so that the correct
        values are returned.
        """
        point = (3,2.5)
        y = utils.gety(point)
        self.assertEqual(2.5, y)

    def test_shift_point(self):
        """
        Test that a point is being properly shifted
         when calling utils.shift_point
        """
        point = (0,0)
        new_point = utils.shift_point(point, 3, 4)
        self.assertEqual((3,4), new_point)

        point = (-2.34, 1.19)
        new_point = utils.shift_point(point, 2.34, -1.19)
        self.assertEqual((0,0), new_point)
