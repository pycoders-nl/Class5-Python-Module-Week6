"""**client.py**
- You will have class `Client` inside this file.
- Class `Client` will have `account` dictionary as the class variable. 
This dictionary will keep following info: "account_number, name, total_amount"
- `__init__` method will initialize this variables, it will take `name` and `total_amount` 
as params and will assign a random 5 digit int to `account_number`
- Lastly this class will have `withdraw`, `deposit` and `balance` methods."""
import random

class Client:
    #This class about bank clients. All Atm's processed here.
    account = dict()  #Dict. holds all data .
    def __init__(self,name,total_amount):
        self.name = name
        self.total_amount = total_amount
        self.account_number = random.randint(10000,99999) #Random turned account number
        print(f"Account created successfully! Your account number is: {self.account_number} ")
        Client.account[str(self.account_number)] = {"name" : self.name , "total_amount" : self.total_amount} #It saved like {"clientaccount_number" : {"name" : clientname , "total_amount": clienttotal_amount}}
    def updatetotalamount(self):
        """Whenever total amount changed , this function worked and updated total_amount in account's dictionary"""
        Client.account.update({str(self.account_number) : {"total_amount" : self.total_amount}})
        print(f"Succesfull . Your new balance : {self.total_amount} ")
    def withdraw(self,amount):
        """to Withdraw money but first check balance of money"""
        try : 
            self.checkbalance(amount)
        except ValueError as Nomoney:
            print (Nomoney)
        else : 
            self.total_amount = self.total_amount - amount
            print(f"Withdrawing .. {amount}")
            self.updatetotalamount()
    def deposit(self,amount):
        """deposit money"""
        self.total_amount += amount
        print(f"Depositing .. {amount}")
        self.updatetotalamount()
    def balance (self):
        return self.total_amount
    def checkbalance(self,amount):
        if self.total_amount < amount : 
            raise ValueError("Not Enough money")
