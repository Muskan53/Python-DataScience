# Topic: Adding labels and titles


import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 5)
plt.plot(x, x, x, x*4, x, x/2)
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.title("This is the title")
plt.show()
