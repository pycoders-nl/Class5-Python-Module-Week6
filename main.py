from bank import Bank
from client import Client
print("""Welcome to International Bank!""")

international_bank = Bank("International")
while True : 
    print(""" Choose an option:
    1. Open new bank account
    2. Open existing bank account
    3. Exit""")
    choice = input (" Your choice : ")
    if choice == "1" : 
        name = input ("Name : ")
        total_amount = int(input ("Deposit Amount : "))
        client = Client(name,total_amount) #Created new client
        international_bank.add_client(client) #Client object's way sended to bank system (bank_client_list) . 
    elif choice == "2" :
        print("To access your account, please enter your credentials below.")
        name = input ("Name : ")
        account_number = int(input("Account Number : "))
        if international_bank.authentication(name,account_number): #confirmed to informations.
            print(f"Authentication successful!\nWelcome {name} ")
            while True : 
                """
                def accessobject(func):
                    for i in Bank.clients:
                        i.func(func)"""
                print("""Choose an option:\n1. Withdraw\n2. Deposit\n3. Balance\n4. Exit""")
                choice2 = input ("Your choice : ")
                if choice2 == "1" :
                    withdraw = int(input("Withdraw Amount : "))
                    for i in Bank.clients:
                        #i is a class of client's object way. we can reach that client's methods
                        if i.name == name and i.account_number == account_number : 
                            i.withdraw(withdraw)
                elif choice2 == "2" : 
                    deposit = int(input("Deposit Amount : "))
                    for i in Bank.clients:
                        if i.name == name and i.account_number == account_number : 
                            i.deposit(deposit)
                elif choice2 == "3": 
                    for i in Bank.clients:
                        if i.name == name and i.account_number == account_number : 
                            print(i.balance())
                elif choice2 == "4":
                    break
                else : 
                    print("Valid Error")
    elif choice == "3" : 
        print("Have a nice day")
        break
    else :
        print("Valid Error")
