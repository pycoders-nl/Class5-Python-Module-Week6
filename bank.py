lass Bank:
    __clients = []
    def __init__(self,name):
        self.name = name
    def add_client(self,client):
        self.__clients.append(client)
    def authentication(self,name,account_number):
        self.name = name
        self.account_number = account_number
    def getclient(self):
        self.__clients
