import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import argparse

# create the parser
parser = argparse.ArgumentParser(description='Visualize a 3D point cloud from a CSV file.')
parser.add_argument('file', type=str, help='The path to the CSV file')

# parse the command-line arguments
args = parser.parse_args()

# read the csv file using pandas
df = pd.read_csv(args.file, header=None)

# considering that your csv file has three columns for the coordinates
x = df[0].values
y = df[1].values
z = df[2].values

# create a 3d scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z,s=1)

# Setting the axes properties for equal axes
max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0

mid_x = (x.max()+x.min()) * 0.5
mid_y = (y.max()+y.min()) * 0.5
mid_z = (z.max()+z.min()) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# optionally set the title of your graph
ax.set_title('3D Point Cloud')

# show the plot
plt.show()
