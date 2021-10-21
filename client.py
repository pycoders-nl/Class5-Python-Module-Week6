from random import randint

class Client:#I defined a class Client
    account={}
    
    def __init__(self,name,total_amount):#Class Client have account_number, name, total_amount attributes
       
        self.account["name"]=name
        self.account["balance"]=total_amount
        self.account["account_number"]=randint(10000,99999)# assign a random 5 digit int to account_number

    def withdraw(self,amount): #withdraw, deposit and balance methods.
        
        self.account["balance"] -=amount
        print(f"the sum of {amount} has been withdrawn from your account balance")
        
        self.balance()

   


    def deposit(self,amount):
        
        
        self.account["balance"] += amount
        print(f"the sum of {amount} has been added to your account balance")
        self.balance()

   
    
    
    def balance(self):
        print("Your current account balance is: {} ".format(self.account["balance"]))

        
