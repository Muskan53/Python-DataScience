# Topic: Adding multiple graphs

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.plot([1, 2, 3, 4], [2, 3, 4, 5])
plt.plot([1, 2, 3, 4], [3, 4, 5, 6])
plt.show()

# or

plt.plot([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [2, 3, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6])
plt.show()

# Line 12 can also be written using range function as follows:
# This makes easy to make changes in it in future.

x = range(1, 5)
plt.plot(x, x, x, [i+1 for i in x], x, [i+2 for i in x])
plt.show()
