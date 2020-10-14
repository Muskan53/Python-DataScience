# Topic: Creating Pie Charts

import matplotlib.pyplot as plt


plt.figure(figsize=(5, 5))

labels = ["USA", "India", "China", "Italy", "Canada"]
values = [25, 10, 15, 40, 23]

explode = [.1, 0, .05, .05, 0]
plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode, colors=["c", "g", "y", "m", "b"])
plt.show()
