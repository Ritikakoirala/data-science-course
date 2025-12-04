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