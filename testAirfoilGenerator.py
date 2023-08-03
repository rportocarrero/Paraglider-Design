# This program creates a set of points that defines a dummy airfoil.  
import math
import matplotlib.pyplot as plt
import numpy as np

h, k = 0, 0  # Center of the circle
r = 0.05  # Radius of the circle

# Generate points
n = 100  # Number of points
angles = np.linspace(np.pi/2, 3*np.pi/2, n)
LE_points = [(h + r * math.cos(i), k + r * math.sin(i)) for i in angles]

d = 0.95 / (n - 1)  # Spacing between points
top_Points = [(i * d, r) for i in range(n)]  # Generate points

# Separate the x and y values
LE_points_x, LE_points_y = zip(*LE_points)
top_Points_x, top_Points_y = zip(*top_Points)

# List the points in proper order
for i in reversed(top_Points):
    print(i)
for i in (LE_points):
    print(i)

import csv

# List the points in proper order
points = [i for i in reversed(top_Points)] + [i for i in LE_points]

# Open a file for writing
with open('testAirfoilPoints.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for point in points:
        writer.writerow(point)


