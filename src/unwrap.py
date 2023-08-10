from src.pointRotation import *
from src.panelAlignment import *

def unwrap(inboard_airfoil_points, outboard_airfoil_points):
    points = []
    # for each panel rotate and align
    for i in range(len(inboard_airfoil_points)-1):
        #first triangular panel
        rotated_points = np.array(rotate_points([inboard_airfoil_points[i], outboard_airfoil_points[i], outboard_airfoil_points[i+1]]))
        rotated_points=rotated_points[:,0:2]
        alignment_vector = [inboard_airfoil_points[i],outboard_airfoil_points[i]]
        alignment_vector = [point[:2] for point in alignment_vector]
        new_points = alignPanel(alignment_vector,rotated_points)
        for point in new_points:
            points.append(point)

        #second triangular panel
        rotated_points = np.array(rotate_points([inboard_airfoil_points[i], outboard_airfoil_points[i+1], outboard_airfoil_points[i+1]]))
        rotated_points=rotated_points[:,0:2]
        alignment_vector = np.array([inboard_airfoil_points[i],outboard_airfoil_points[i+1]])
        alignment_vector = alignment_vector[:,0:2]
        new_points = alignPanel(alignment_vector,rotated_points)
        for point in new_points:
            points.append(point)

    return points

# # Test the unwrap function
#inboard_test_points = np.array([[0,0,0],[1,0,0],[2,0,0]])
#outboard_test_points = np.array([[0,1,0],[1,1,0],[2,1,0]])

#UnwrappedPoints = unwrap(inboard_test_points, outboard_test_points)
#print(UnwrappedPoints)