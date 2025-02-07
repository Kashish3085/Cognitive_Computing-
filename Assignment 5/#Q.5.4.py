# 4
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 1)

plt.figure(figsize=(10, 6))

plt.plot(x, y1, label=r'$Y = x^2$', color='blue')
plt.plot(x, y2, label=r'$Y = \sin(x)$', color='green')
plt.plot(x, y3, label=r'$Y = e^x$', color='red')
plt.plot(x, y4, label=r'$Y = \log(|x| + 1)$', color='purple')

plt.title("Function Plots using NumPy and Matplotlib", fontsize=14)
plt.xlabel("X values", fontsize=12)
plt.ylabel("Y values", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.show()
