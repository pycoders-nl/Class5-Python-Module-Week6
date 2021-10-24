# - You will have class `Client` inside this file.
# - Class `Client` will have `account_number`, `name`, `total_amount` attributes
# - `__init__` method will initialize these variables, it will take `name` and
#  `total_amount` as params and will assign a random 5 digit int to `account_number`
# - Lastly this class will have `withdraw`, `deposit` and `balance` methods.

import random
import string
from bank import Bank


class Client:

    def __init__(self,name,total_amount):
        self.name = name
        self.total_amount = total_amount
        self.account_number = random.randint(10000,99999)
        
        b1 = Bank(self.name)
        b1.add_client(self.account_number,self.name,self.total_amount)
        print(f'Account created successfully! Your account number is: {self.account_number}')
    


    def withdraw(self,account_number,amount):
        self.account_number = account_number
        self.amount = amount
        for i in range(len(Bank.clients)):
            if self.account_number==Bank.clients[i][0]:
                Bank.clients[i][2] -= self.amount
                self.total_amount = Bank.clients[i][2]
                print(f'The sum of {self.amount} has been withdrawn from your account balance.')
                print(f'Your current account balance is: {self.total_amount}')
    
    def deposit(self,account_number,amount):
        self.account_number = account_number
        self.amount = amount
        for i in range(len(Bank.clients)):
            if self.account_number==Bank.clients[i][0]:
                Bank.clients[i][2] += self.amount
                self.total_amount = Bank.clients[i][2]
                print(f'The sum of {self.amount} has been added to your account balance.')
                print(f'Your current account balance is: {self.total_amount}')

    def balance(self,account_number):
        self.account_number = account_number
        for i in range(len(Bank.clients)):
            if self.account_number==Bank.clients[i][0]:
                self.total_amount = Bank.clients[i][2]
                print(f'Your current account balance is: {Bank.clients[i][2]}')

