class Bank:

    clients = []

    def __init__(self, name):
        self.name = name

    def add_client(self, client):
        self.clients.append(client)

    def authentication(self, name, account_number):
        for i in range(len(self.clients)):
            if name == self.clients[i].name and account_number == self.clients[i].account_number:
                print("Authentication successful!")
                return self.clients[i]

        print('''
    Authentication failed!
    Reason: account not found.
    ''')
    