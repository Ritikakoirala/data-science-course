#account
user = {
    "sanju": 100000,
    "karuna": 200000,
    "sumina": 2000000
}
username = input("Enter your name: ")
if username in user:
    print("You are logged in..")

    operation = input("Enter your queray (balance_check, add_balance, withdraw): ")

    match operation:
        case "balance_check":
            print("Your balance is:", user.get(username))
        case "add_balance":
            new = int(input("Enter amount to add: "))
            user[username] += new
            print("New balance:", user.get(username))
        case "withdraw":
            amount = int(input("Enter withdraw amount: "))
            if amount <= user[username]:
                user[username] -= amount
                print("Withdraw successful. Remaining balance:", user.get(username))
            else:
                print("Amount is not sufficient!")
        case _:
            print("Invalid operation!")

else:
    print("Try again, username not found.")






#calculator in loop
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
select_operation=input("enter the operation like sub sum div etc:").split()
for operation in select_operation:
    if operation =="sum":
        print(a+b)
    elif operation =="sub": 
        print(a-b)
    elif operation =="mul":
        print(a*b)
    elif operation =="div":
        print(a/b)
    elif operation =="mod":
        print(a%b)
    else :
        print(a**b)                  


#list in loop

names = ["smita", "jennifer", "swikriti", "seybica"]
name = input("Enter your name: ")
for user in names:
    if user == name:
        print("User is present")
        break
else:
    print("User is not present")
     



#dictinorey in loop
   
dict={
    "sanju":123,
    "karuna":345,
    "sunima":678
} 
 
username=input("enter the name :")
for i in dict:
    if i==username:
        print("user found")
        break
    else:
        print("try again...")
        break


#calculator using while
while True:
    a = int(input("enter the number:"))
    b = int(input("enter the number:"))
    operation = input("enter the operation")
    if operation == "sum":
        print(a + b)
    elif operation == "sub":
        print(a - b)
    elif operation == "mul":
        print(a * b)
    elif operation == "div":
        print(a / b)
    else:
        break




#calculator
a=int(input("enter a first number:"))
b=int(input("enter the second number:"))
add=a+b
print(add)
sub=a-b
print(sub)
mul=a*b
print(mul)
div=a/b
print(div)
mod=a%b
print(mod)
exp=a**b
print(exp)




#calculator using function
first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
def sum(first,second):
    print(first+second)
def sub(first,second):
    print(first-second)
def mul(first,second):
    print(first*second)
def div(first,second):
    print(first/second)   
sum(first,second)
sub(first,second)
mul(first,second)
div(first,second)          



#multiplication table
number = int(input("enter the number which you want multiplication table:"))
for i in range(1, 11): 
    print(f"{number} x {i} = {number * i}")
    
#even or odd
a=int(input("enter the number to check odd or even:"))
if a%2==0:
    print("it is the even number ") 
else :
    print("it is the odd number") 
      



#palindrom
num=input("enter the number:")
if str(num) == str(num)[::-1]:
    print("palindrom")
else:
    print("it is not")    
    




#login in or not
data = {
    "sanju": 123,
    "karuna": 345,
    "sumina": 897
}
def registration(username, password):
    print(" username:", username)
    print(" password:", password)
username = input("Enter your username: ")
password = int(input("Enter your password: "))
registration(username, password)
if username in data and data[username] == password:
    print("You are login")
else:
    print("Login failed")
    





#print all the even number from the list    

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is not")
        






#Make a login system using registration using function
users = {}   
def register():
    username = input("Enter a username:")
    if username in users:
        print("Username already exists")
        return

    password = input("Enter a password: ")
    users[username] = password
    print(" successful")
    

def login():
    username = input("Enter username:")
    password = input("Enter password:")

    if username in users and users[username] == password:
        print("successful", username)
    else:
        print("Invalid username or password")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice== "1":
        register()
    elif choice== "2":
        login()
    elif choice== "3":
        break
    else:
        print(" Try again.")






#user register
user=[]
def register():
    username = input("Enter a username:")
    if username not in user :
        print("user not  present")
        user.append(username)
        print("now you are resgister")
        print(user)
    else:
        print("hello",username)
        print("you are already present")

while True:
    choice=input("enter your choice:  register for 1 and exit for 2:")
    if choice=="1":
        register()
    elif choice=="2":
        break
    else:
        print("try again")






#username is present in the list or not
name_list=["ritika","sanju","karuna","sumina"]
user_input=input("enter your name:")
if user_input in name_list:
 print("name is present")
else:
 print("name is not present")  






#dictonary of username and password
data={
    "ritika":123,
    "sanju":345,
    "karuna":678,
    "sumina":912}
user=(data.keys())
username=input("enter your name:")
if username in data:
 print("it is present")
else:
 print("it is not present")




#match calculator
a=int(input("Enter the value for a:"))
b=int(input("enter the value for b:"))
operation=input("enter the operation:")
match operation:
  case "sum":
    print(a+b)
  case "sub":
    print(a-b)
  case "mul":
    print(a*b)   
  case "div":
    print(a/b)
  case "mod":
    print(a%b)
  case "exp":
    print(a**b)






#calculator with if and else
a=int(input("enter the first number:"))
b=int(input("enter the seconf number:"))
operation=input("enter the operation(sum,sub,mul,div):")
if operation == "sum":
    print(a+b)
elif operation == "sub":
    print(a-b)        
elif operation == "mul":
    print(a*b)
else:
    print(a/b)    







#disctonery with if else
data={
    "ritika":123,
    "sanju":456,
    "karuna":789
}
user=data.keys()
username=input("enter your name:")
if username == user:
    print("you are login..")
else:
    print("try againn..")    






#gratest among three
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b:
    if a > c:
        print("a is the greatest")
    else:
        print("c is the greatest")
else:
    if b > c:
        print("b is the greatest")
    else:
        print("c is the greatest")

#Task: Create a Simple Book Class
class book:
    def infromation_about_books(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f"title is {self.title} and the author is{self.author}")

book1=book()
book1.infromation_about_books("python","ram")           
book1.display()






#try and except in python
try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    select_operation=input("enter the operation like sub sum div etc:").split()
    for operation in select_operation:
        if operation =="sum":
            print(a+b)
        elif operation =="sub": 
            print(a-b)
        elif operation =="mul":
            print(a*b)
        elif operation =="div":
            print(a/b)
        elif operation =="mod":
            print(a%b)
    else :
        print(a**b)                  
except Exception as e:
    print(e)


    


#dictinory in try catch
try:
    data = {
    "sanju": 123,
    "karuna": 345,
    "sumina": 897
}
    def registration(username, password):
        print(" username:", username)
        print(" password:", password)
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    registration(username, password)
    if username in data and data[username] == password:
        print("You are login")
    else:
        print("Login failed")
    
except Exception as e:
    print(e)





#match in try catch
try:
    user=[]
    def register():
        username = input("Enter a username:")
    if username not in user :
        print("user not  present")
        user.append(username)
        print("now you are resgister")
        print(user)
    else:
        print("hello",username)
        print("you are already present")

    while True:
        choice=input("enter your choice:  register for 1 and exit for 2:")
    if choice=="1":
        register()
    elif choice=="2":
        break
    else:
        print("try again")
except exception as e:
    print(e)        