"""**bank.py**

- You will have class `Bank`. This bank will have instance variable `name` and class variable 
`clients` list. Initially this list will be empty.
- This class will have method `add_client` method which appends the client to list
- And lastly this class will have `authentication` method which takes `name` and `account_number`
as parameters and authenticates the client"""
from client import Client
class Bank:
    """This class contact with atm and has connection with center."""
    clients = list()  #This list contain client class object's .
    def __init__(self,name):
        self.name = name
    @classmethod
    def add_client(cls,name):
        #sended clients object from main file.
        cls.clients.append(name)

    def authentication(self,name,account_number):
        try :
            if Client.account[str(account_number)]["name"] == name : #it goes client class dict and checks name and account numbers. 
                return True    
        except KeyError : 
            print("Authentication failed! \nReason: Account not found.")
        else : 
            print("Authentication failed! \nReason: Name not found.")
