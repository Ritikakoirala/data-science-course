#Task: Create a Simple Bank Account Class
class bank:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("insufficient balance")
    def display(self):
        print(f"account number is {self.account_number} and the balance is {self.balance}")
bank1=bank(123456,1000)
bank1.deposit(500)
bank1.withdraw(200)
bank1.display()