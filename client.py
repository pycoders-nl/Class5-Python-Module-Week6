import random
random_list=list(set(random.randint(10000,99999) for i in range(9999)))
class Client:
    i = 0
    def __init__(self, name, total_amount):
        self.name = name
        self.total_amount = total_amount
        self.account_number = random_list[Client.i]
        self.account={'n':self.name,'ta':self.total_amount,"an":self.account_number}
        Client.i += 1
    def withdraw(self,amount):
        if self.total_amount >= amount:
            self.total_amount -= amount
            print(f"The sum of {amount} has been withdraw from your account balance.\
            Your current account balance is: {self.total_amount}")
        else:
            print("\n Insufficient balance ")
    def deposit(self,amount):
        self.total_amount = self.total_amount + amount
        print(f"The sum of {amount} has been added to your account balance.\
        Your current account balance is: {self.total_amount}")
    def balance(self,balance):
        self.total_amount = balance
        print(f"Your current account balance is: {self.total_amount}")
