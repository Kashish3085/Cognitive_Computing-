#Assignment 6 
# Q.6.1

import numpy as np
import matplotlib.pyplot as plt

M = float(input("Enter the value of M for the mathematical function: "))

x = np.linspace(-10, 10, 500)

y1 = M * x ** 2         # y = M * x^2
y2 = M * np.sin(x)      # y = M * sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="y = M * x^2", color="blue", linestyle="--")
plt.plot(x, y2, label="y = M * sin(x)", color="red", linestyle="-")

plt.title("Plot of y = M * x^2 and y = M * sin(x) (M = {M})")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.grid(True)

plt.show()
