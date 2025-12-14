#5.Create a 3D array of shape (2, 3, 4) filled with random integers between 1 and 100
import numpy as np
import numpy as np
a = np.random.randint(1, 101, size=(2, 3, 4))
print(a)


#Create a 3x3 matrix with values from 1 to 9(2d array):
mat= np.matrix(np.arange(1,10).reshape(3,3))
print(mat)


#. Create an array of 10 random floats between 0 and 1, and round to 2 decimal places.
a = np.random.random(10)
a = np.round(a, 2)
print(a)



#3.Find all even numbers in the array [1, 3, 6, 9, 12, 15] using Boolean indexing
arr = np.array([1, 3, 6, 9, 12, 15])
even = arr[arr % 2 == 0]=True
print(even)

#4.. Create a 4x4 matrix filled with 7
mat = np.full((4, 4), 7)
print(mat)



#6.From the array below, extract all elements greater than 50 and replace them with -1
arr=np.arange(0,101)
arr[arr >= 50] = -1
print(arr)



#Create a 3D array of shape (3, 4, 5) filled with random integers between 1 and 100.
arr = np.random.randint(1, 101, size=(3, 4, 5))
print(arr)


#Replace all elements greater than the mean of the entire array with 0.
arr = np.array([1, 3, 6, 9, 12, 15])
mean= arr.mean()
arr[arr > mean] = 0
print(arr)



#Calculate the sum along axis=1 (i.e., sum across the 5 columns in each depth slice).

arr = np.array([
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15]],

    [[16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25],
     [26, 27, 28, 29, 30]]
])
axis1 = arr.sum(axis=1)
print(axis1)

#Extract a new 2D array that contains only the first and last columns from each row of each depth slice.
last=arr[:, :, [0, -1]]
print(last)

#Create a NumPy array of numbers from 10 to 50.
array=np.arange(10,51)
print(array)

#Generate a 3×3 identity matrix.
array=np.identity(3)
print(array)

#Create a NumPy array of 10 random integers between 1 and 100.
a=np.random.randint(1,101)
print(a)


#Find the maximum and minimum of an array.
rr = np.array([10, 20, 30, 40, 50])
print(rr.max())
print(rr.min())


 #a 1D array of 12 elements into a 3×4 matrix.
arr1d = np.arange(1, 13)
matrix = arr1d.reshape(3, 4)
print(matrix)


#Create an array of all even numbers between 50 and 100.
arr = np.arange(50, 101)       
even = arr[arr % 2 == 0]       
print(even)


#Given an array [1,2,3,4,5], compute the square of each element.
arr = np.array([1, 2, 3, 4, 5])
squared = arr ** 2
print(squared)


#Create a 5×5 array of random numbers and find its mean.
random_array = np.random.random((5, 5))  
mean_val=random_array.mean()
print(random_array)
print(mean_val)



#Find the index of the maximum element in [10, 20, 50, 40, 30].
arr = np.array([10, 20, 50, 40, 30])
max = arr.argmax()
print(max)


#Create two arrays and perform element-wise addition, subtraction, multiplication, and division.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)
print(a * b)
print(a / b)


