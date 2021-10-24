# This class initially will create a bank object with a name you choose and
# then will print the following menu (it should print this menu, until user says exit) 


from bank import Bank
from client import Client
import time

while True:
    print('''
    Welcome to International Bank!

Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
    ''')
    kies_1 = int(input('your choise : '))
    if kies_1 == 1:
        print('''
        To create an account, please fill in the information below.
        ''')
        a = str(input('Name: '))
        b = int(input('Deposit amount: '))
        Client(a,b)
        

    elif kies_1 == 2:
        print('''
        To access your account, please enter your credentials below.
        ''')
        while True:
            name = input('Name: ')
            account_number =int(input('Account Number: '))
            authen = Bank.authentication(Bank,name,account_number)
            if authen == True:
                print('Authentication successful!')
                break
            else:
                print('Authentication failed!\nReason: account not found.')
                

                continue
                
        while True:
            print(f'''
            Welcome {name}!

            Choose an option:

                1. Withdraw
                2. Deposit
                3. Balance
                4. Exit
            ''')
            kies_2 = int(input('your choise : '))
            if kies_2 == 1:
                amount = int(input('Withdraw amount: '))
                Client.withdraw(Client,account_number,amount)
                time.sleep(2)
                
            elif kies_2 ==2:
                deposit = int(input('Deposit amount: '))
                Client.deposit(Client,account_number,deposit)
                time.sleep(2)
                
            elif kies_2 == 3:
                Client.balance(Client,account_number)
                time.sleep(2)

            elif kies_2 == 4:
                break

                
        
    elif kies_1 == 3:
        break
