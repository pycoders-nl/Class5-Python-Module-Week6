class Bank:
    clients=[]
    def __init__(self,name):
        self.name=name
    def add_client(self,client):    
        self.clients.append(client) 
    def authentication(self,name,account_number):
        pass
    def clients(self):
        print(self.clients)

