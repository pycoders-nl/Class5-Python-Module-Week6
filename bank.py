class Bank: #I defined class Bank.  
    clients=[] #clients list and it is now empty
    def __init__(self,name): #This bank will have instance variable name and class variable clients list.
        self.name=name
        
    
    def add_client(self,client):#Class have method add_client method which appends the client to list
        self.clients.append(client)

    def authentication(self,name,account_number):#authentication method which takes name and account_number as parameters a
    #and authenticates the client
        self.name=name
        self.account_number=account_number
        
        for i in range(len(self.clients)):
            client=self.clients[i]
          
            if (name==client.account["name"]) and (account_number==client.account["account_number"]):
                print("Authentication is succesful")
                return self.clients[i]