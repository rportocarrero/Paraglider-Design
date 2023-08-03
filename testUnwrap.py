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
scale_factor = 5
P1_points = [(x*scale_factor, y*scale_factor) for (x, y) in points]
#print("Airfoil 1 points: ")
#for i in P1_points:
    #print(i)


# Generate the points for the second airfoil profile
scale_factor = 4
P2_points = [(x*scale_factor, y*scale_factor) for (x, y) in points]
#print("Airfoil 2 points: ")
#for i in P2_points:
    #print(i)


# Add the cell distance parameter to turn the airfoild profiles into 3d.
D = 1 #cell width
P1_points = [(x, 0, y) for (x, y) in P1_points]
P2_points = [(x, D, y) for (x, y) in P2_points]
#print("Airfoil 1 points: ")
#for i in P1_points:
    #print(i)
# Open a file for writing
with open('Airfoil1_Points.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for point in P1_points:
        writer.writerow(point)

#print("Airfoil 2 points: ")
#for i in P2_points:
    #print(i)
# Open a file for writing
with open('Airfoil2_points.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for point in P2_points:
        writer.writerow(point)

# Display surface profiles
# Panel surface
with open('CellPanels.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for point in P1_points:
        writer.writerow(point)
    for point in P2_points:
        writer.writerow(point)

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
#print("Normal vectors: ")
#for vector in normal_vectors:
    #print(vector)
# Open a file for writing
with open('normal_Vectors.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for vector in normal_vectors:
        writer.writerow(vector)

# Initialize an empty list to store all axes of rotation
axes_of_rotation = []

# Iterate over all normal vectors
for normal_vector in normal_vectors:
    # Compute the axis of rotation for the current panel
    rot_axis = np.cross(normal_vector, [0, 0, 1])

    # Append the axis of rotation to the list
    axes_of_rotation.append(rot_axis)

# Display the axis of rotation
print("Axes of rotation: ")
for rotax in axes_of_rotation:
    print(f"{rotax}")

# Open a file for writing
with open('rotationAxis.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for vector in axes_of_rotation:
        writer.writerow(vector)

# Initialize list to store angles of rotation
angles_of_rotation = []

# Calculate and store the angle of rotation for each panel
for i in range(len(normal_vectors)):
    rot_angle = np.arccos(np.dot(normal_vectors[i], axes_of_rotation[i]))
    angles_of_rotation.append(rot_angle)

# Open a file for writing
with open('rotationAngles.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for angle in angles_of_rotation:
        writer.writerow([angle])  # Pass angle as a single-item list

print("Rotating the points")
import numpy as np

def rotation_matrix(axis_of_rotation, rot_angle):
    # unpack the axis of rotation
    x, y, z = axis_of_rotation

    R = np.array([
        [np.cos(rot_angle) + x**2 * (1 - np.cos(rot_angle)), x*y*(1 - np.cos(rot_angle)) - z*np.sin(rot_angle), x*z*(1 - np.cos(rot_angle)) + y*np.sin(rot_angle)],
        [x*y*(1 - np.cos(rot_angle)) + z*np.sin(rot_angle), np.cos(rot_angle) + y**2 * (1 - np.cos(rot_angle)), y*z*(1 - np.cos(rot_angle)) - x*np.sin(rot_angle)],
        [x*z*(1 - np.cos(rot_angle)) - y*np.sin(rot_angle), y*z*(1 - np.cos(rot_angle)) + x*np.sin(rot_angle), np.cos(rot_angle) + z**2 * (1 - np.cos(rot_angle))]
    ])

    return R


# rotate the points
P1_points_rotated = []
P2_points_rotated = []

for i in range(len(P1_points)-1):
    # generate the rotation matrix for this point
    R = rotation_matrix(axes_of_rotation[i], angles_of_rotation[i])
    # append the rotated points
    P1_points_rotated.append(np.dot(R, P1_points[i]))
    P2_points_rotated.append(np.dot(R, P2_points[i]))

# Open a file for writing
with open('Rotatedpoints.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for point in P1_points_rotated:
        writer.writerow(point)
    for point in P2_points_rotated:
        writer.writerow(point)


