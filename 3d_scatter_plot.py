# Topic: Creating 3D Scatter Plots

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


fig = plt.figure()
chart = fig.add_subplot(1, 1, 1, projection="3d")
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)
size = 100*np.random.rand(100)
colors = np.random.rand(100)

chart.scatter(x, y, z, s=size)
# chart.scatter(x, y, z, s=size, c=colors, marker="^")
plt.show()
