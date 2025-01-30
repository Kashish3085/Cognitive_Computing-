# Q.4.2

import numpy as np

# Reverse
arr = np.array([1,2,3,6,4,5])
r = arr[::1]
print("Reversed Array:",r,"\n")

# Frequency

def most_fre(a):
    f = np.bincount(a).argmax()
    print("Most Frequent Value:",f)
    i = np.where(a==f)[0]
    print("Indices:",i,"\n")

x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1,1,1,2,3,4,2,4,3,3])
most_fre(x)
most_fre(y)