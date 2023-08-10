import unittest
import src.panelAlignment as pa
import numpy as np

class testAlign(unittest.TestCase):
    def test_sanityCheck(self):
        self.assertEqual(1,1)

    def test_rotationOnly(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[0,0],[0,1],[-1,1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8)  

    def test_translationOnly(self):
        edgePoints = np.array([[0,2],[1,2]])
        panelPoints = np.array([[0,0],[1,0],[1,1]])
        expected_points = np.array([[0,2],[1,2],[1,3]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translationAndRotation(self):
        edgePoints = np.array([[2,2],[3,2]])
        panelPoints = np.array([[0,0],[0,-1],[-1,1]])
        expected_points = np.array([[2,2],[3,2],[3,3]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 