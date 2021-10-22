import random

class Client():
    data_base={}      #We keep clients as 'no : name,amount'
    def __init__(self,name,total_amount):
        self.name=name
        self.total_amount=total_amount
        self.acc_No=(''.join(random.sample('0123456789', 5)))#we assign 5 digits number as str
        print("Account created successfully! Your account number is: %s "%(self.acc_No))
        Client.data_base[self.acc_No]={"name" : self.name ,"total_amount" : self.total_amount}
    def updated_amount(self):    #We need to save in dictionary current amount after transactions
        Client.data_base.update({self.acc_No : {"total_amount" : self.total_amount}})
        print("Transaction done.Now,you have  : %s"% (self.total_amount))

    
    def withdraw(self,amount):
            self.total_amount -= amount
            if amount>self.total_amount:
              raise "insufficient balance"
            else:
                self.updated_amount() 
   
    def deposit(self,amount):
        self.total_amount+=amount
        print("%s has been added your account."%(amount))
        self.updated_amount()


    def balance(self):
        s='Name :%s , Account Number : %s ,Current Balance : %d '%(self.name,self.acc_No,self.total_amount)
        print(s)

