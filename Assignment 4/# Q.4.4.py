# Q.4.4

import numpy as np

kash = np.linspace(10,100,25)

print("Array: ",kash,"\n")
print("Dimensions: ",kash.ndim,"\n")
print("Shape: ",kash.shape,"\n")
print("Total Elements: ",kash.size,"\n")
print("Data Type: ",kash.dtype,"\n")
print("Total Bytes: ",kash.nbytes,"\n")

t = kash.reshape(25,1)
print("Using Reshape: \n",t)

tt = kash.T
print("Using T Attribute:\n ",tt)

