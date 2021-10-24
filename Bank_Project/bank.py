#* - You will have class `Bank`. This bank will have instance variable `name` 
#* and class variable `clients` list. Initially this list will be empty.
#* - This class will have method `add_client` method which appends the client to list
#* - And lastly this class will have `authentication` method which takes 
#* `name` and `account_number` as parameters and authenticates the client



class Bank:
    clients = [[11111,'aaa',1000], [22222,'bbb',2000], [33333,'ccc',3000]]
    def __init__(self,name):
        self.name = name
    
    def add_client(self,account_number,name,total_amount):
        self.name = name
        self.total_amount = total_amount
        self.account_number = account_number
        Bank.clients.append([self.account_number,self.name,self.total_amount])


    def authentication(self,name,account_number):
        self.name = name
        self.account_number = account_number
        # for i in range(len(self.clients)):
        #     if (self.account_number == self.clients[i][0] and self.name == self.clients[i][1]):
        #         return True
        for i in self.clients:
            if i[0] == self.account_number and i[1] == self.name:
                return True
