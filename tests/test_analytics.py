import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        rangeValues = [1,2,3,4,1,2,3,4]
        self.permutations = analytics.permutations(99)
        self.upper, self.lower = analytics.compute_critical(rangeValues)
        
        #avgNNPoints = ([1,2],[3,4],[5,6])
        


        def test_permutations(self):
            self.assertEqual(len(permutations), 99)
            self.assertNotEqual(permutations[0], permutations[1])

        def test_compute_critical(self):
            self.assertTrue(lower == 1)
            self.assertTrue(upper == 4)
            self.assertTrue(observed_avg < lower or observed_avg > upper)

        def test_check_significant(self):

            significance = [analytics.check_significant(self.lower, self.upper, 3)]

            self.assertTrue(significance[1])
            self.assertFalse(significance[0])
            

        
