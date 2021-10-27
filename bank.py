import time
class Bank:
    __clients=[]
    def __init__(self,name):
        self.name=name

    def add_clients(self,client):
        self.__clients.append(client)

    def authentication(self,name,account_number):
        for i in range(len(self.__clients)):
            if name == self.__clients[i].name and account_number == self.__clients[i].account_number:
                time.sleep(1)
                print("Authentication successful!")
                return self.__clients[i]
        print('''
    Authentication failed!
    Reason: account not found.
    ''')

    def getclients(self):
        return self.__clients