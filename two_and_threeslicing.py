#Implement 2d and 3d slicing for a 3d array

import numpy as np
arr = np.arange(27).reshape(3,3,3)
print(arr)
print(arr[0, :, :])
print(arr[:, 0, :])
print(arr[:, :, 0])
print(arr[0, 0, :])
print(arr[0, 0, :])
print(arr[1, 1, :])
print(arr[1, 2, :])
print(arr[1, 0, :])
