# This file is used to rotate the panels of the mesh to align with the z-axis

import numpy as np

# Find the normal vector for the panel
def find_normal_vector(c1,c2,c3):
    # find the cross-product
    U=[c-b for c,b in zip(c3,c2)]
    V=[a-b for b,a in zip(c2,c1)]

    N=np.cross(U,V)
    # normalize the vector
    N=[a/np.linalg.norm(N) for a in N]
    return N

# Find the rotation axis for the panel
def find_rotation_axis(normal_vector):
    rot_axis = np.cross(normal_vector, [0, 0, 1])
    return rot_axis/np.linalg.norm(rot_axis)

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


