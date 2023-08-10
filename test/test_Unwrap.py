import unittest
import numpy as np
import src.unwrap as u

class testUnwrap(unittest.TestCase):
    def test_sanityCheck(self):
        self.assertEqual(1,1)

    def test_unwrap(self):
        inboard_test_points = np.array([[0,0,0],[0,1,0],[0,2,0]])
        outboard_test_points = np.array([[1,0,0],[1,1,0],[1,2,0]])
        expected_points = np.array([[0,0],[1,0],[2,0],[1,0],[1,1],[1,2]])
        UnwrappedPoints = u.unwrap(inboard_test_points, outboard_test_points)
        np.testing.assert_allclose(expected_points, UnwrappedPoints, atol=1e-8)  

