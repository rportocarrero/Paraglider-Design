import numpy as np
import csv

# Planform Parameters:
A=3.5
B=1.5
C=0.8
span=7
Cells=20

# Generate Points on the Ellipse

# equations for leading edge planform
def LEplanform(x, A, B):
    y=B*np.sqrt(1-(x/A)**2)
    return y

# equations for trailing edge planform
def TEplanform(x, A, C):
    y=-C*np.sqrt(1-(x/A)**2)
    return y

dx=span/(Cells-1)

# Generate points on the leading edge
LE_points = [(i, LEplanform(i, A, B),0) for i in np.arange(0, span/2, dx)]
# Generate points on the trailing edge
TE_points = [(i, TEplanform(i, A, C),0) for i in np.arange(0, span/2, dx)]

# Open a file for writing
with open('PlanformPoints.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for point in LE_points:
        writer.writerow(point)
    for point in TE_points:
        writer.writerow(point)

#Load airfoil 
# Read in the airfoil points from the CSV file
Airfoil_points = []

# Open the file for reading
with open('testAirfoilPoints.csv', 'r') as f:
    reader = csv.reader(f)

    # Read points from the CSV file
    for row in reader:
        Airfoil_points.append((float(row[0]), float(row[1])))

# for each planform point, add the airfoil points to create the wing planform
Planform_points=[]

for i in range(len(LE_points)):
    # obtain chord length
    chord=LE_points[i][1]-TE_points[i][1]

    # scale airfoil points to chord length
    Airfoil_points_scaled = [(x*chord, y*chord) for (x, y) in Airfoil_points]
    #translate points to 

    # add the cell distance parameter to turn the airfoil profiles into 3d.
    for(x,y) in Airfoil_points_scaled:
        offset=LE_points[i][1]
        Planform_points.append([-x+offset,dx*i,y])
    
with open('FullWing.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the points to the CSV file
    for point in Planform_points:
        writer.writerow(point)