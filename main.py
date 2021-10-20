from client import Client
from bank import Bank
class main(Bank):    
    b1=Bank(input('Name of Bank: '))
    import time
    print("Welcome to {}".format(b1.name))
    while True:
        print("""Choose an option:
        1. Open new bank account
        2. Open existing bank account
        3. Exit
        """)
        choice=input("")
        if choice=='3':
            break
        
        elif choice=='1':
            name_=input("Name: ")
            t_amount=int(input("Total amount: "))
            client1=Client(name_, t_amount)
            b1.add_clients(client1.account)
            time.sleep(1)
            print("Account created successfully! Your account number is: {}".format(client1.account['account_number']))
        elif choice=='2':
            account_number=int(input("Account number: "))
            name=input("Name: ")
            client_authentication=b1.authentication(name,account_number)
            if client_authentication:
                print("Bank account is opening...")
                time.sleep(1)
                print('Welcome {}'.format(name))
                for i in range(len(b1.getclients())):
                    if b1.getclients()[i]['account_number']==account_number:
                        break
                while True:
                    print("""Choose an option:
            1. Withdraw
            2. Deposit
            3. Balance
            4. Exit""")
                    choice1=input("Choice: ")
                    if choice1=='1':
                        b1.getclients()[i]['total_amount']=Client(b1.getclients()[i]['name'],b1.getclients()[i]['total_amount']).withdrawn(int(input("Withdrawn amount: ")))                    
                    elif choice1=='2':
                        b1.getclients()[i]['total_amount']=Client(b1.getclients()[i]['name'],b1.getclients()[i]['total_amount']).deposit(int(input("Deposit amount: ")))
                    elif choice1=='3':
                        Client(b1.getclients()[i]['name'],b1.getclients()[i]['total_amount']).current_balance()
                    elif choice1=="4":
                        break
            else:
                time.sleep(1)
                print('Authentication failed! \nReason: account is not found')
m=main()