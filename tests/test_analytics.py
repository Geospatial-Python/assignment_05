import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics
from .. import io_geojson


class TestFilesAndDicts(unittest.TestCase):
    """
    This set of tests is focused on reading some geojson
    data in as a Python dictionary and then answering
    some questions about the data.
    """

    @classmethod
    def setUpClass(cls):
        cls.gj = io_geojson.read_geojson('data/us_cities.geojson')

    def test_read_geojson(self):
        self.assertIsInstance(self.gj, dict)

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
        self.assertTrue(some_return,308473.3217503218)


class TestAnalytics(unittest.TestCase):

   # def setUp(self):
    #    pass

    @classmethod
    def setUpClass(cls):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        cls.points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]

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