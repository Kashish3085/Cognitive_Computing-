# 2
import numpy as np

# Part (a)
array = np.array([10, 52, 62, 16, 16, 54, 453])

# i. Sorted array
sorted_array = np.sort(array)

# ii. Indices of sorted array
sorted_indices = np.argsort(array)

# iii. 4 smallest elements
smallest_4 = np.sort(array)[:4]

# iv. 5 largest elements
largest_5 = np.sort(array)[-5:]

print("Sorted array:", sorted_array)
print("Indices of sorted array:", sorted_indices)
print("4 smallest elements:", smallest_4)
print("5 largest elements:", largest_5)

# Part (b)
array_b = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# i. Integer elements only
integer_elements = array_b[array_b == array_b.astype(int)]

# ii. Float elements only
float_elements = array_b[array_b != array_b.astype(int)]

print("Integer elements only:", integer_elements)
print("Float elements only:", float_elements)
