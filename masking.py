#Extract the last 3 elements from the array
array=(1,2,3,4,5,6,7,8,9)
a=array[-3:]
print(a)

import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])



#1.Slice and print every third element starting from index 1.
print(arr[1::3])

#2.Print the last 4 elements using negative indexing.
print(arr[-4:])

#3.Replace the values at even indices with -1
arr[arr%2 == 0] = -1
print(arr)


#Fancy indexing to extract positions [2, 4, 6, 8]
a = arr[[2, 4, 6, 8]]
print(a)








