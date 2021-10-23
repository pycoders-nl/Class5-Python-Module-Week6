from client import Client
from bank import Bank

class Main(Bank):
    bank = Bank(input("Please chosee a name of Bank: "))
    print(f"Welcome to {bank.name} Bank!\nChoose an option:")
    while True:
        menu = input("1. Open new bank account\n2. Open existing account\n3. Exit\nPlease code a number!: ")
        if menu == "1":
            print("To create an account, please fill in the information below.")
            name_c = input("Name: ")
            deposit_amount = int(input("Deposit amount: "))
            client = Client(name_c, deposit_amount)
            bank.add_client(client.account)
            print(f"Account created successfully! Your account number is: {client.account['an']}")
        elif menu == "2":
            while True:
                print("To access your account, please enter your credentials below.")
                name = input("Name: ")
                account_number = int(input("Account Number: "))
                if name != name and account_number != account_number:
                    print("Authentication failed!\nReason: account not found.")
                else:
                    name == name and account_number == account_number
                    print(input(f"Authentication successful!\nWelcome {name}\nChoose an option:\n1. Withdraw\n2. Deposit\n3. Balance\n4. Exit\nPlease code a number!: "))
                    while True:
                        if input == "1":
                            withdraw = input("Withdraw amount:")
                            print(f"The sum of {withdraw} has been withdraw from your account balance.\
                                Your current account balance is: {total_amont}")
                        
                        elif input == "2":
                            deposit = input("Deposit amount: ")
                            print(f"The sum of {deposit} has been added to your account balance.\
                                Your current account balance is: {total_amount}")
                        
                        elif input == "3":
                            print(f"Your current account balance is: {total_amount}")

                        elif input == "4":
                            print("Exit...")
                        
                        else:
                            print("Enter a correct value from given type help for commands")
        else:
            menu == "3"
            break
