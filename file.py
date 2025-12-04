import json

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    cred = {username: password}
    file = open("credentials.txt", "a")
    file.write(json.dumps(cred) + "-")
    file.close()

    
    bal = {username: 0}
    file = open("balance.txt", "a")
    file.write(json.dumps(bal) + "-")
    file.close()

    print("Registration successful")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    file = open("credentials.txt", "r")
    content = file.read()
    file.close()
    users_list = content.split("-")

   
    file = open("balance.txt", "r")
    bal_content = file.read()
    file.close()
    bal_list = bal_content.split("-")

    
    balance = 0
    for b in bal_list:
        if b.strip() == "":
            continue
        bd = json.loads(b)
        if username in bd:
            balance = bd[username]

    for user_data in users_list:
        if user_data.strip() == "":
            continue

        data = json.loads(user_data)

        if username in data and data[username] == password:
            print("Login successful!")

            operation = input("Enter your query (balance_check, add_balance, withdraw): ")
        while True:
            match operation:
                case "balance_check":
                    print("Your balance is:", balance)

                case "add_balance":
                    new = int(input("Enter amount to add: "))
                    balance += new
                    print("New balance:", balance)

                case "withdraw":
                    amount = int(input("Enter withdraw amount: "))
                    if amount <= balance:
                        balance -= amount
                        print("Withdraw successful. Remaining balance:", balance)
                    else:
                        print("Amount is not sufficient!")
                case "break":
                    exit    
                case _:
                    print("Invalid operation")

           
            updated = ""
            for b in bal_list:
                if b.strip() == "":
                    continue
                bd = json.loads(b)
                if username in bd:
                    bd[username] = balance
                updated += json.dumps(bd) + "-"
            
            file = open("balance.txt", "w")
            file.write(updated)
            file.close()

            return

    print("Try again...")


while True:
    choice = int(input("Enter 1 for register, 2 for login, 3 for exit: "))
    match choice:
        case 1:
            register()
        case 2:
            login()
        case 3:
            print("Exit")
            break
        case _:
            print("Invalid choice")
