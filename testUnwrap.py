import numpy as np
import csv
import matplotlib.pyplot as plt

# Read in the airfoil points from the CSV file

points = []

# Open the file for reading
with open('testAirfoilPoints.csv', 'r') as f:
    reader = csv.reader(f)

    # Read points from the CSV file
    for row in reader:
        points.append((float(row[0]), float(row[1])))

print(points)


# Generate the points for the first airfoil profile
scale_factor = 10
P1_points = [(x*scale_factor, y*scale_factor) for (x, y) in points]
print("Airfoil 1 points: ")
for i in P1_points:
    print(i)


# Generate the points for the second airfoil profile
scale_factor = 1
P2_points = [(x*scale_factor, y*scale_factor) for (x, y) in points]
print("Airfoil 2 points: ")
for i in P2_points:
    print(i)

# Add the cell distance parameter to turn the airfoild profiles into 3d.
D = 1 #cell width
P1_points = [(x, 0, y) for (x, y) in P1_points]
P2_points = [(x, D, y) for (x, y) in P2_points]
print("Airfoil 1 points: ")
for i in P1_points:
    print(i)

print("Airfoil 2 points: ")
for i in P2_points:
    print(i)

# assuming P1_points and P2_points are lists of points defining the panels
normal_vectors = []

# Find the normal vector for the panel
def find_normal_vector(c1,c2,c3):
    # find the cross-product
    U=[b-a for a,b in zip(c1,c3)]
    V=[c-a for a,c in zip(c1,c2)]

    N=np.cross(U,V)
    # normalize the vector
    N=[a/np.linalg.norm(N) for a in N]
    return N

# Find the normal vectors for each panel
for i in range(len(P1_points)-1):
    normal_vector = find_normal_vector(P1_points[i], P1_points[i+1],P2_points[i])
    normal_vectors.append(normal_vector)

# Display the normal vectors
print("Normal vectors: ")
for vector in normal_vectors:
    print(vector)

# Find the axis of rotation for each panel
print("finding axis of rotation")
axis_of_rotation = []
for i in range(len(normal_vectors)):
    axis_of_rotation.append(np.cross(normal_vectors[i],[0,0,1]))

# Display the axis of rotation
print("Axis of rotation: ")
for vector in axis_of_rotation:
    print(vector)

# Display the angle of rotation
print("Angle of rotation: ")
for i in range(len(normal_vectors)):
    # Normalize the vectors
    normal_vector_norm = normal_vectors[i] / np.linalg.norm(normal_vectors[i])
    axis_of_rotation_norm = axis_of_rotation[i] / np.linalg.norm(axis_of_rotation[i])
    # Calculate the angle
    rot_angle = np.arccos(np.clip(np.dot(normal_vector_norm, axis_of_rotation_norm), -1.0, 1.0))
    print(rot_angle)