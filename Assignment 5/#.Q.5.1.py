# NUMPY
#1 
import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

# Sum of all elements
total_sum = gfg.sum()

# Row-wise sum
row_wise_sum = gfg.sum(axis=1)

# Column-wise sum
column_wise_sum = gfg.sum(axis=0)

print("Sum of all elements:", total_sum)
print("Row-wise sum:", row_wise_sum)
print("Column-wise sum:", column_wise_sum)
