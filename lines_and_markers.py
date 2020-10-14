# Topic: Line and Marker Customization

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 5)
plt.plot(x, x, "--o", label="Medium", color="c")
plt.plot(x, x*4, "-.+", label="Fast", color="green")
plt.plot(x, x/2, "r:*", label="Slow")
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.title("This is title")
plt.legend(loc="best")
plt.grid(True)
plt.axis([0, 4.5, -1, 16.5])
plt.show()
