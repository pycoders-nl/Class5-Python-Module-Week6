from client import Client

class Bank(Client):
    clients=[]  # clients will be stored as its unique path in memory, not as name
    
    def __init__(self, name):
        self.name=name 
        
        
        
    @classmethod
    def add_client(cls,client):
        cls.client=client
        cls.clients.append(client)
        
    
    def authentication(self,name,acc_No): #account number key to verify its name from database dict in CLient class
        try :
            if Client.data_base[acc_No]["name"] == name :  
                return True    
        except KeyError : 
            print("Authentication failed! \nReason: Account not found.")


