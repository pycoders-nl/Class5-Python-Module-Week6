'''**client.py**
- You will have class `Client` inside this file.
- Class `Client` will have `account_number`, `name`, `total_amount` attributes
- `__init__` method will initialize these variables, 
it will take `name` and `total_amount` as params and will assign a random 5 digit int to `account_number`
- Lastly this class will have `withdraw`, `deposit` and `balance` methods.'''

import random

rnd_list=list(set(random.randint(10000,99999) for i in range(9999)))

class Client:
    i=0
    def __init__(self, name, total_amount):

        self.name=name
        self.total_amount=total_amount
        self.account_number=rnd_list[Client.i]
        self.account={'name':self.name,'total_amount':self.total_amount,"account_number":self.account_number}
        Client.i+=1

    def withdraw(self,amount):
        amount=float(input("Enter withdraw amount :"))
        if self.total_amount >= amount:
            self.account -=amount
            print(f"The sum of {amount} has been withdrawn from your account balance.")
            print(f"Current account balance is : {self.total_amount}")
        
        else:
            print("Current account balance is not enough.")
            return self.account
        

    def deposit(self,amount):

        amount=float(input("Enter deposit amount :"))
        self.total_amount+=amount
        print(f"The sum of {amount} has been added to your account balance.")
        print(f"Current account balance is : {self.total_amount}")
        return self.total_amount
        
    
    def balance(self):
        print(f"Current account balance is : {self.total_amount}")




client1=Client
print(client1)


