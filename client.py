import random
class Client:
    i=0

    def __init__(self,name,total_amount,account_number = random.randint(10000,99999)):
        self.name = name
        self.account_number = account_number
        self.total_amount = total_amount
        Client.i+=1
    
    def withdraw(self):
        amount = int(input('Enter an amount:'))
        if amount<= self.total_amount and amount>0:
            return f"You have withdrawn {amount}"
        else:
            return f"Invalid request"
    
    def deposit(self):
        amount = int(input('Enter an amount:'))
        if amount >0:
            return f"You have {self.total_amount + amount} in your account."
        else:
            return f"You havent deposited any money."

    def balance(self):
        return f"Your balance is: {self.total_amount}"

# client_1 =Client('halit',10000)
# print(client_1)