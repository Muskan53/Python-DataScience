# Topic: Creating a Legend

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 5)
plt.plot(x, x, x, x*4, x, x/2)
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.title("This is title")
plt.legend(["Medium", "Fast", "Slow"])  # Here we need to remember the order in which graphs are plotted
plt.show()


# If we do not want to remember the order, we can provide legends individually.

plt.plot(x, x, label="Medium")
plt.plot(x, x*4, label="Fast")
plt.plot(x, x/2, label="Slow")
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.title("This is title")
plt.legend()
plt.show()


# We can change the default location(which is upper left) of legends as follows:

plt.plot(x, x, label="Medium")
plt.plot(x, x*4, label="Fast")
plt.plot(x, x/2, label="Slow")
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.title("This is title")
plt.legend(loc="best")
# Best automatically finds the best location to put legends
# Other possible locations are:
#   best
# 	upper right
# 	upper left
# 	upper center
# 	lower right
# 	lower left
# 	lower center
# 	center right
# 	center left
# 	center
# 	right
#   etc.
plt.show()
