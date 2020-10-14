# Topic: Introduction to 3-D Plots

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


fig = plt.figure()
chart = fig.add_subplot(1, 1, 1, projection="3d")
plt.plot([2, 5, 7, 3, 6], [5, 4, 7, 8, 2], [8, 6, 4, 7, 2])
plt.show()
