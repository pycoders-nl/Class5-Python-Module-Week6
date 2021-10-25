'''**bank.py**

- You will have class `Bank`. This bank will have instance variable `name` and class variable `clients` list. Initially this list will be empty.
- This class will have method `add_client` method which appends the client to list
- And lastly this class will have `authentication` method which takes `name` and `account_number` as parameters and authenticates the client'''
from client import Client
class Bank:
    clients = []
    def __init__(self, name):
        self.name = name
    def add_client(self, name):
        self.clients.append(name)
    def authentication(self, name, account_number):
        if Client.account[str(account_number)]["name"] == name :
            print("authentication is succesfull!")
            return True
        else :
            print("Authentication failed! \nReason: Name not found.")
            return False

