import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):

    def setUp(self):

        
        def check_create_random_points():
            self.assertEqual(len(create_random_points), 100)
