# This file is used to rotate the panels of the mesh to align with the z-axis

import numpy as np

# Find the normal vector for the panel
def find_normal_vector(c1,c2,c3):
    # find the cross-product
    U=[c-b for c,b in zip(c3,c2)]
    V=[a-b for b,a in zip(c2,c1)]

    N=np.cross(U,V)
    # normalize the vector
    norm = np.linalg.norm(N)
    N = [a/norm for a in N]
    return N

# Find the rotation axis for the panel
def find_rotation_axis(normal_vector):
    rot_axis = np.cross(normal_vector, [0, 0, 1])
    if np.linalg.norm(rot_axis) == 0:
        rot_axis = [1, 0, 0]
    else:
        rot_axis = rot_axis/np.linalg.norm(rot_axis)
    return rot_axis

# Find the rotation angle for the panel
def find_rotation_angle(normal_vector):
    rot_angle = np.arccos(np.dot(normal_vector, [0, 0, 1]))
    return rot_angle

# function for the skew-symmatrix matrix of a vector
def skew(x):
    return np.array([[0, -x[2], x[1]],
                     [x[2], 0, -x[0]],
                     [-x[1], x[0], 0]])

# derive the Rotation matrix around an arbitrary axis
def rotation_matrix(axis_of_rotation, rot_angle):
    R = (np.cos(rot_angle)*np.identity(3)) + ((1-np.cos(rot_angle))*np.outer(axis_of_rotation, axis_of_rotation)) + (np.sin(rot_angle)*skew(axis_of_rotation))
    return R

# Rotate set of triangular panel points
def rotate_points(points):
    normal_vector=find_normal_vector(points[0], points[1], points[2])
    rot_axis=find_rotation_axis(normal_vector)
    rot_angle=find_rotation_angle(normal_vector)
    R=rotation_matrix(rot_axis, rot_angle)
    rotated_points=[]
    for point in points:
        rotated_points.append(np.dot(R, point))
    return rotated_points

