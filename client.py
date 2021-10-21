import random
class client:
    def __init__(self,account_number,name,total_amount):
        self.account_number=random(5)
        self.name=name
        self.total_amount=random(5)

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.total_amount += amount
        print("\n Amount Deposited:", amount)
    
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.total_amount >= amount:
            self.total_amount -= amount
            print("\n You Withdraw:", amount)
        else:
            print("\n Insufficient balance  ")

    def balance(self):
        print(self.total_amount)
    


