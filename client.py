'''**client.py**
- You will have class `Client` inside this file.
- Class `Client` will have `account_number`, `name`, `total_amount` attributes
- `__init__` method will initialize these variables, it will take `name` and `total_amount` as params and will assign a random 5 digit int to `account_number`
- Lastly this class will have `withdraw`, `deposit` and `balance` methods.
'''
import random
class Client:
    account={}
    def __init__(self, name, total_amount):
        self.name=name
        self.total_amount=total_amount
        self.account_number = random.randint(10000,99999)
        print(f"Account created successfully! Your account number is: {self.account_number} ")
        Client.account[str(self.account_number)] = {"name" : self.name , "total_amount" : self.total_amount}
    '''def newaccount(self):
        Client.account.update({str(self.account_number) : {"total_amount" : self.total_amount}})
        print(f"Succesfull . Your new balance : {self.total_amount} ")'''
    def withdraw(self, amount):
        if self.total_amount > amount :
            self.total_amount -= amount
            print(f"\nThe sum of {amount} has been withdrawn from your account balance")
            print(f"Your current account balance is: {self.total_amount}")
            return self.total_amount
        else:
            return "Insufficient funds"
    def deposit(self, amount):
        self.total_amount+= amount
        print(f"The sum of {amount} has been added to your account balance.")
        print(f"Your current account balance is: {self.total_amount}")
        return self.total_amount
    def balance(self):
        print ("Your current account balance is: {self.total_amount}") 