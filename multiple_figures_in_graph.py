# Topic: Multiple Figures in a Graph
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

chart1 = fig.add_subplot(3, 1, 1)
chart2 = fig.add_subplot(3, 1, 2)
chart3 = fig.add_subplot(3, 1, 3)

x = np.arange(1, 5)
chart1.plot(x, x, "--o", label="Medium", color="c")
chart2.plot(x, x*4, "-.+", label="Fast", color="green")
chart3.plot(x, x/2, color="r", linestyle=":", label="Slow", linewidth=5.0,
         marker="d", markersize=10.0, markeredgecolor="b", markerfacecolor="c")
# plt.xlabel("This is x-axis")
# plt.ylabel("This is y-axis")
# plt.title("This is title")
plt.legend(loc="best")
plt.grid(True)
plt.axis([0, 4.5, -1, 16.5])
plt.show()
