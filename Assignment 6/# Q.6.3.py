# Q.6.3

import numpy as np
import matplotlib.pyplot as plt

roll_number = 102317116
np.random.seed(roll_number)

data = np.random.randn(50)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(np.cumsum(data), color="blue", linestyle="-", marker="o")
axes[0, 0].set_title("Cumulative Sum Plot")
axes[0, 0].set_xlabel("Index")
axes[0, 0].set_ylabel("Cumulative Sum")
axes[0, 0].grid(True)

noise = np.random.randn(50)
axes[0, 1].scatter(range(50), data + noise, color="green", alpha=0.7)
axes[0, 1].set_title("Scatter Plot with Random Noise")
axes[0, 1].set_xlabel("Index")
axes[0, 1].set_ylabel("Value + Noise")
axes[0, 1].grid(True)

axes[1, 0].axis("off")
axes[1, 1].axis("off")

plt.tight_layout()

plt.show()
