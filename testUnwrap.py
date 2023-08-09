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

airfoil_points = points

# write points to file
def write_points_file(filename, points):
    # Open a file for writing
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the points to the CSV file
        for point in points:
            writer.writerow(point)

# Generate the points for the first airfoil profile
scale_factor = 5
P1_points = [(x*scale_factor, y*scale_factor) for (x, y) in airfoil_points]

# Generate the points for the second airfoil profile
scale_factor = 4
P2_points = [(x*scale_factor, y*scale_factor) for (x, y) in airfoil_points]

# Add the cell distance parameter to turn the airfoild profiles into 3d.
D = 1 #cell width
P1_points = [(x, 0, y) for (x, y) in P1_points]
P2_points = [(x, D, y) for (x, y) in P2_points]

# write points to file
write_points_file('Airfoil2_points.csv', P2_points)

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
    U=[c-b for c,b in zip(c3,c2)]
    V=[a-b for b,a in zip(c2,c1)]

    N=np.cross(U,V)
    # normalize the vector
    N=[a/np.linalg.norm(N) for a in N]
    return N

# Find the normal vectors for each panel
for i in range(len(P1_points)-1):
    normal_vector = find_normal_vector(P1_points[i], P2_points[i],P2_points[i+1])
    normal_vectors.append(normal_vector)

# write normal vectors to file
write_points_file('normal_Vectors.csv', normal_vectors)

# Initialize an empty list to store all axes of rotation
axes_of_rotation = []

def find_rotation_axis(normal_vector):
    rot_axis = np.cross(normal_vector, [0, 0, 1])
    return rot_axis/np.linalg.norm(rot_axis)

# Iterate over all normal vectors
for normal_vector in normal_vectors:
    # Append the axis of rotation to the list
    axes_of_rotation.append(find_rotation_axis(normal_vector))

# Display the axis of rotation
#print("Axes of rotation: ")
#for rotax in axes_of_rotation:
#    print(f"{rotax}")

# write axes of rotation to file
write_points_file('rotationAxis.csv', axes_of_rotation)

# Initialize list to store angles of rotation
angles_of_rotation = []

#calculate rotation angle
def find_rotation_angle(normal_vector):
    rot_angle = np.arccos(np.dot(normal_vector, [0, 0, 1]))
    return rot_angle

# Calculate and store the angle of rotation for each panel
for i in range(len(normal_vectors)):
    angles_of_rotation.append(find_rotation_angle(normal_vectors[i]))

# Open a file for writing
with open('rotationAngles.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for angle in angles_of_rotation:
        writer.writerow([angle])  # Pass angle as a single-item list

# function for the skew-symmatrix matrix of a vector
def skew(x):
    return np.array([[0, -x[2], x[1]],
                     [x[2], 0, -x[0]],
                     [-x[1], x[0], 0]])

# derive the Rotation matrix around an arbitrary axis
def rotation_matrix(axis_of_rotation, rot_angle):
    R = (np.cos(rot_angle)*np.identity(3)) + ((1-np.cos(rot_angle))*np.outer(axis_of_rotation, axis_of_rotation)) + (np.sin(rot_angle)*skew(axis_of_rotation))
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


test_points = [[0,0,0],[1,0,0],[1,1,1],[0,1,1]]
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

for point in rotated_points:
    print(f'Rotated Point:{point}')