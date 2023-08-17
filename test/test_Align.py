import unittest
import src.panelAlignment as pa
import numpy as np
import csv

# strip comments from csv file
def non_comment_lines(file):
    for line in file:
        # Ignore lines that start with the comment character #
        if not line.strip().startswith('#'):
            yield line

class testFirstTriangleAlign(unittest.TestCase):
    def test_sanityCheck(self):
        self.assertEqual(1,1)

    def rotation_test(self, row):
        edgePoints = np.array([[row[0],row[1]],[row[2],row[3]]])
        panelPoints = np.array([[row[4],row[5]],[row[6],row[7]],[row[8],row[9]]])
        expected_points = np.array([[row[10],row[11]],[row[12],row[13]],[row[14],row[15]]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8)

    # Rotation Tests
    def test_rotation(self):
        with open('test/test_data/first_triangle_rotation_tests.csv', 'r') as file:
            filtered_lines = non_comment_lines(file)
            reader = csv.reader(filtered_lines)
            for row in reader:
                rotation_test(self, row)

    # Translation Tests
    def test_translation1(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[0,0],[1,0],[1,1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translation2(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[1,1],[2,1],[2,2]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translation3(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[1,0],[2,0],[2,1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translation4(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[1,-1],[2,-1],[2,0]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translation5(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[0,-1],[1,-1],[1,0]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translation6(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[-1,-1],[0,-1],[0,0]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translation7(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[-1,0],[0,0],[0,1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    def test_translation8(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[-1,1],[0,1],[0,2]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

class testSecondTriangleAlign(unittest.TestCase):
    # rotation tests
    def test_rotation1(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[0,0],[1,0],[1,1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8)  

    def test_rotation2(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[0,0],[0,1],[-1,1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8)

    def test_rotation3(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[0,0],[-1,0],[-1,-1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8)  

    def test_rotation4(self):
        edgePoints = np.array([[0,0],[1,0]])
        panelPoints = np.array([[0,0],[0,-1],[1,-1]])
        expected_points = np.array([[0,0],[1,0],[1,1]])
        aligned_points = pa.alignPanel(edgePoints, panelPoints)
        np.testing.assert_allclose(expected_points, aligned_points, atol=1e-8) 

    