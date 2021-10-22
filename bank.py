'''**bank.py**

- You will have class `Bank`. This bank will have instance variable `name` and class variable `clients` list.
Initially this list will be empty.
- This class will have method `add_client` method which appends the client to list
- And lastly this class will have `authentication` method 
which takes `name` and `account_number` as parameters and authenticates the client
'''


from client import Client


class Bank:
    clients=[]

    def __init__(self,name):
        self.name=name

    def add_client(self,client):
        self.clients.append(client)
    
    def authentication(self,name,account_number):
        for i in range(len(self.clients)):
            if name==self.clients[i]['name'] and  account_number==self.clients[i]['account_number']:
                print("Authentication successful!")
                return self.clients[i]
            else:
                print("Authentication not successful!")