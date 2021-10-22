
from client import Client
from bank import Bank


class main(Bank):
    bank_name=Bank(input("Name of Bank : "))
    print(f"Welcome to {bank_name}")

    while True:

        print("""Choose an option:
        1. Open new bank account
        2. Open existing bank account
        3. Exit
        """)
        demands=int(input("Please Enter you want to transaction : "))

        if demands==1:
            name=input("Name :")
            new_amount=int(input("Your amount :"))
            customer1=Client(name,new_amount)
            bank_name.add_client(customer1.account)
            print(f"Account created successfully.Your account number is {customer1.account['account_number']}")

        elif demands==2:
            name=input("Name :")
            account_number=int(input("Enter your account number :"))
            ##clint_credentials=bank_name.authentication(name,account_number)

            while True:
                print("""Choose an transaction
            1. Withdraw,
            2. Deposit
            3. Balance
            4. Exit""")

                transaction=int(input("Please choice transsaction :"))

                if transaction==1:
                    Client.deposit()
            
                elif transaction == 2:
                    Client.withdraw(1)
                elif transaction == 3:
                    Client.balance()
                else:
                    break
        else :
            print("Have a Nice Day!")
            break 