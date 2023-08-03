import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
ax.scatter(x, y, z)

# optionally set the title of your graph
ax.set_title('3D Point Cloud')

# show the plot
plt.show()
