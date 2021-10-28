from random import randint

class Client:

    available_nums = []

    def __init__(self, name, total_amount):
        self.name = name
        self.total_amount = total_amount
        self.account_number = self.generate_random()
        self.available_nums.append(self.account_number)

    def generate_random(self):
        num = randint(10000, 99999)
        while num in self.available_nums:
            num = randint(10000, 99999)
        return num

    def withdraw(self, amount):
        if self.total_amount >= amount:
            self.total_amount -= amount
            print(f"The sum of {amount} has been withdrawn from your account balance.")
            self.balance()
        else:
            print("Not enough money!")

    def deposit(self, amount):
        self.total_amount += amount
        print(f"The sum of {amount} has been added to your account balance.")
        self.balance()

    def balance(self):
        print(f"Your current account balance is: {self.total_amount}")
        return self.total_amount

