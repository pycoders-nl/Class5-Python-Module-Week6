import random
random_list=list(set(random.randint(10000,99999) for i in range(9999)))
class Client:
    i=0
    def __init__(self,name,total_amount):
        self.name=name
        self.total_amount=total_amount
        self.account_number=random_list[Client.i]
        Client.i+=1
    def withdrawn(self,amount):
        if self.total_amount>=amount:
            self.total_amount-=amount
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
            self.current_balance()
            return self.total_amount
        else:
            print("Your current account balance is not enough.")
    def deposit(self,amount):
        self.total_amount+=amount
        print("The sum of {} has been added to your account balance.".format(amount))
        self.current_balance()
        return self.total_amount

    def current_balance(self):
        print ("Your current account balance is: {}".format(self.total_amount))