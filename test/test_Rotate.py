import unittest
import src.pointRotation as pr
import numpy as np

class testTriangleRotation(unittest.TestCase):
    def test_sanityCheck(self):
        self.assertEqual(1,1)

    def test_noRotation(self):
        points = [[0,0,0],[1,0,0],[1,1,0]]
        rotated_points = pr.rotate_points(points)
        np.testing.assert_allclose(points, rotated_points, atol=1e-8)

    def test_90DegRotation(self):
        test_points = [[0,0,0],[1,0,0],[1,0,1]]
        expected_points = [[0,0,0],[1,0,0],[1,1,0]]
        rotated_points = pr.rotate_points(test_points)
        np.testing.assert_allclose(expected_points, rotated_points, atol=1e-8)   