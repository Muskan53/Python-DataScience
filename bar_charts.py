# Topic: Creating Bar Charts

import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(10, 5))

names = ["Alan", "Jacob", "Clay", "Edward", "Mark"]
scores = [90, 82, 85, 96, 78]
scores2 = [92, 86, 80, 75, 88]

positions = np.arange(len(scores))  # positions = [0 1 2 3 4]

plt.bar(positions, scores, width=0.2, color="c")
plt.bar(positions+0.2, scores2, width=0.2, color="m")
plt.xlabel("Names")
plt.ylabel("Scores")
plt.title("Latest Test Score")
plt.xticks(positions+0.1, names)
plt.show()
