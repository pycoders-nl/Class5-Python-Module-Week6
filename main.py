from client import Client
from bank import Bank
import time

b1=Bank(input('Name of Bank: '))

available=True   
while available:
    print("Welcome to {}".format(b1.name))
    print("""Choose an option:
        1. Open new bank account
        2. Open existing bank account
        3. Exit
        """)
    choice=int(input("1,2,3: "))
    if choice==3:
            available = False
    elif choice==1:
        print("To create an account, please fill in the information below.")
        name_=input("Name: ")
        t_amount=int(input("Total amount: "))
        client1=Client(name_, t_amount)
        b1.add_clients(client1)
        time.sleep(1)
        print("Account created successfully! Your account number is: {}".format(client1.account_number))
    elif choice==2:
        print("To access your account, please enter your credentials below.")            
        account_number=int(input("Account number: "))
        name=input("Name: ")
        client_authentication=b1.authentication(name,account_number)
        if client_authentication:
            authorized = True
            print("Bank account is opening...")
            time.sleep(1)
            print('Welcome {}'.format(name))
            while authorized:
                print("""Choose an option:
            1. Withdraw
            2. Deposit
            3. Balance
            4. Exit""")
                choice1=int(input("Choice: "))
                if choice1==1:
                    w_amount = int(input("Withdraw amount:"))
                    client_authentication.withdrawn(w_amount)
                elif choice1==2:
                    d_amount = int(input("Deposit amount:"))
                    client_authentication.deposit(d_amount)
                elif choice1==3:
                    client_authentication.current_balance()
                elif choice1==4:
                    authorized=False
            
        else:
            time.sleep(1)
            print('Authentication failed! \nReason: account is not found')
        
