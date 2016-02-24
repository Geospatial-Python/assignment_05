import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

#from .. import utils
import utils
import random


class TestUtils(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        i = 0
        self.points = []
        while i < 100:
            seed = (round(random.random(),2), round(random.random(),2))
            self.points.append(seed)
            n_additional = random.randint(5,10)
            i += 1
            c = random.choice([0,1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt = (round(seed[0] + x_offset, 2), round(seed[1] + y_offset,2))
                    self.points.append(pt)
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break

    def test_create_random(self):
        rand_points = utils.create_random(100)
        self.assertEqual(100, len(rand_points))

    def test_permutations(self):
        permutations = utils.permutations(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])
