# Topic: Creating Histograms

import matplotlib.pyplot as plt
import numpy as np


x = np.random.randn(1000)
# plt.hist(x)
# plt.hist(x, bins=20, color="c")
# plt.hist(x, bins=[-3, 0, 3], color="c")
plt.hist(x, bins=20, color="c", cumulative=True)
plt.show()
