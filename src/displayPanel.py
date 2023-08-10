# This python file is used to troubleshoot the unwrapping algorithm

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import art3d
from pointRotation import *
import numpy as np


# Create figure and axes
fid = plt.figure()
ax = fid.add_subplot(111, projection='3d')

test_points = [[0,0,0],[1,0,0],[1,0,1]]
print(f'Test Points: {test_points}')

normal_vector = find_normal_vector(test_points[0], test_points[1], test_points[2])
print(f'Normal Vector: {normal_vector}')

rot_axis = find_rotation_axis(normal_vector)
print(f'Rotation Axis:{rot_axis}')

rot_angle = find_rotation_angle(normal_vector)
print(f'Rotation Angle:{rot_angle}')

rot_matrix = rotation_matrix(rot_axis, rot_angle)
print(f'Rotation Matrix:{rot_matrix}')

# Rotate the points
rotated_points=[]
for point in test_points:
    rotated_points.append(np.dot(rot_matrix, point))

rotated_points = rotate_points(test_points)

# Display the panel
original_panel = art3d.Poly3DCollection([test_points])
rotated_panel = art3d.Poly3DCollection([rotated_points])
ax.add_collection3d(original_panel)
ax.add_collection3d(rotated_panel)
ax.quiver(*[0,0,0], *normal_vector, color='b', length=1.0, normalize=True)
ax.quiver(*[0,0,0], *rot_axis, color='r', length=1.0, normalize=True)

plt.show()