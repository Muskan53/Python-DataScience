# Topic: Creating 3D Bar Charts

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


fig = plt.figure()
chart = fig.add_subplot(1, 1, 1, projection="3d")

x = [1, 2, 3, 4, 5]
y = [2, 8, 2, 5, 7]
z = [0, 0, 0, 0, 0]

dx = np.ones(5)  # [1, 1, 1, 1, 1]
dy = np.ones(5)
dz = [3, 4, 5, 6, 7]

chart.bar3d(x, y, z, dx, dy, dz, color="#47ef54")
chart.set_xlabel("X-Label")
chart.set_ylabel("Y-Label")
chart.set_zlabel("Z-Label")
plt.show()
