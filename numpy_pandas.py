#Create a NumPy array of numbers from 10 to 50.
import numpy as np
arr=np.arange(10,51)
print(arr)


#Generate a 3×3 identity matrix.
arrr=np.arange(100).reshape(5,5,4)
print(arrr)


#Create a NumPy array of 10 random integers between 1 and 100
arrrr=np.random.randint(1,101,10)
print(arrrr)



#Find the maximum and minimum of an array.
ar=np.random.randint(1,50,10)
print(ar)
maximum=np.max(ar)
minimum=np.min(ar)
print("Maximum value:", maximum)
print("Minimum value:", minimum)


#Reshape a 1D array of 12 elements into a 3×4 matrix.
a=np.arange(1,13)
matrix=a.reshape(3,4)
print(matrix)


#Create an array of all even numbers between 50 and 100.
a=np.arange(50,101)
a=arr[arr%2==0]
print("even:",a)

# Given an array [1,2,3,4,5], compute the square of each element.
array=[1,2,3,4,5]
array=np.square(array)
print(array)


#Create a 5×5 array of random numbers and find its mean.
array= np.random.randint(1, 101, (5, 5)) 
mean= np.mean(array)
print("5×5 :", array)
print("Mean:", mean)


#find the index of the maximum element in [10, 20, 50, 40, 30].
array=[10, 20, 50, 40, 30]
arr=np.argmax(array)
print(arr)


#Create two arrays and perform element-wise addition, subtraction, multiplication, and division.
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 5, 8])
print(arr1)
print(arr2)
addition = arr1 + arr2
print("Addition:", addition)
subtraction = arr1 - arr2
print("Subtraction:", subtraction)
multiplication = arr1 * arr2
print("Multiplication:", multiplication)
division = arr1 / arr2
print("Division:", division)



#pandas 
#Create a Pandas DataFrame from a dictionary of lists.
import pandas as pd   
df=pd.DataFrame({

"Name": ["rohan", "roshni", "rose"],

'Department': ['head_chef', 'commi', 'intern']})
print(df)



#Read a CSV file into a DataFrame and display the first 5 rows.
import pandas as pd
data=pd.read_csv("Salary_Data.csv")
print(data.head())


#Get the number of rows and columns of a DataFrame
print(data.shape)


#Display all column names and their data types.
print(data.dtypes)


#Select a single column ('Name') and multiple columns ('Name', 'Age') from a DataFrame.
a=data[["Education Level","Age"]]
print(a)


#Select the first 3 rows using iloc.
first = data.iloc[:3]
print(first)



#Find missing values in a DataFrame.
values=data.isnull()
print("Missing:\n",values)
count=data.isnull().sum()
print("\nNumber of missing :\n",count)


#Replace all NaN values with "Unknown".
filled=data.fillna("Unknown")
print(filled)



#Sort the DataFrame by the 'Age' column in descending order.
sorted=data.sort_values(by='Age', ascending=False)
print(sorted)



#Group the DataFrame by 'Department' and calculate the average salary.
average_salary=data.groupby('Job Title')['Salary'].mean()
print(average_salary)
