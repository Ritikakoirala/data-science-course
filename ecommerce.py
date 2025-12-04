def register():
    name=input("enter your name:")
    password=input("enter your password:")
    with open("user.txt", "a") as file:
        file.write(f"{name},{password}\n")
    print("registration succesfull")

def login():
    username=input("enter your name:")
    password_input=input("enter your password:")
    with open("user.txt", "r") as file:
        for line in file:
            name,password = line.strip().split(",")
            if name==username and password==password_input:
                print("login successful")
                
                
                while True:
                    choice = input("Enter addtocart, viewcart, buynow, or logout:").lower()
                    if choice == "addtocart":
                        add_to_cart()
                    elif choice == "viewcart":
                        view_cart()
                    elif choice == "buy now":
                        buy_now()
                    elif choice == "logout":
                        print("Logged out successfully.")
                        break
                    else:
                        print("invalid input")
                return  
    print("invalid name or password")

def add_to_cart():
    productname=input("enter the product name: ")
    price=input("enter the price: ")
    with open("cart.txt", "a") as file:
        file.write(f"{productname},{price}\n")
    print("product added to cart")

def view_cart():
    with open("cart.txt", "r") as file:
        for line in file:
            productname,price = line.strip().split(",")
            print(f"product name: {productname}, price: {price}")

def buy_now():
    with open("cart.txt", "r") as file:
        for line in file:
            productname, price = line.strip().split(",")
            print(f"product name: {productname}, price: {price}")


while True:
    choice = input("Enter 1 for register, 2 for login, 3 to exit: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("invalid input")
