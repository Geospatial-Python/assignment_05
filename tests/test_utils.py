import unittest

from ..import utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.random_points = utils.create_random_points(100)
        self.permutations = utils.permutation(99)

    def test_create_random(self):
        self.assertEqual(100, len(self.random_points))

    def test_permutation(self):
        self.assertEqual(len(self.permutation), 99)
        self.assertNotEqual(self.permutation[0], self.permutation[1])
