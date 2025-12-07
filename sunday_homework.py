#1.Write a program to read a text file and print each line with line numbers.
with open('sunday_homework.txt',"r") as file:
    line = file.readlines()
    for i in range(len(line)):
        print(f"{i+1} {line[i]}")

#2.Write a program to create a file and write five lines of text into it.
with open("sunday_homework.txt","w") as file:
    file.write('''my name is sourav joshi
             my name is sourav joshi
                  my name is sourav joshi
                  my name is sourav joshi
                  my name is sourav joshi''')
                
#3.Write a program to count the number of words in a given text file.
with open("sunday_homework.txt","r") as file:
    line = file.read()
    word = line.split()
    print(len(word))



#4. Write a program that takes two numbers and handles the error if division by zero occurs.
                
num=int(input("enter the number:"))
num1=int(input("enter the number:"))
try:
    print(num/num1)
except ZeroDivisionError:
    print("zero division")


#5.Write a program that handles the error when trying to open a file that does not exist.
with open("sunday_homework.txt","r") as file:
    try:
        print(file.read())
    except FileNotFoundError:
        print("file not found")



#6.Write a program that asks the user for an integer and handles invalid input.
try:
    num=int(input("enter the number:"))
    print(num)
except ValueError:
    print("invalid input")
        

#7. Create a class with two attributes and print the values using objects.

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
obj=student("ramu",20)
obj.display()
        


#8.create a class with methods to perform basic arithmetic operations and call them.

class arithmetic:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
obj=arithmetic(20,20)
obj.add()
obj.sub()
obj.mul()
obj.div()
        

#9.Create a class with a constructor that initializes two attributes and displays them.


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
obj=student("ramu",20)
obj.display()


#10. Create a parent class and a child class where the child overrides one method.


class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class child(parent):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
obj=child("ramu",20)
obj.display()