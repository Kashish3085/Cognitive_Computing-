# Q.4.5

import numpy as np

ucs402_kash = np.array([[10,20,30,40],[50,60,70,80],[90,15,20,35]])

print("Mean: ",np.mean(ucs402_kash))
print("Median: ",np.median(ucs402_kash))
print("Max: ",np.max(ucs402_kash))
print("Min: ",np.min(ucs402_kash))
print("Unique: ",np.unique(ucs402_kash))

reshaped_ucs402_kash = ucs402_kash.reshape(4,3)
print("Reshape: \n",reshaped_ucs402_kash)

resized_ucs402_kash = np.resize(ucs402_kash,(2,3))
print("Resize: \n",resized_ucs402_kash)