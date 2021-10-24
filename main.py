from bank import Bank
from client import Client
class Main(Bank):
    b=Bank('Rabobank')
    while True:
        print('Welcome to {}','\n','\n','Choose an option:','\n','1.Open a new bank account','\n','2.Open an existing bank account','\n','3.Exit'.format(b))
        number = int(input('Choose an option:'))
        if number== 3:
            break
        elif number == 1:
            print('To create an account please fill in the information below')
            name= input('Enter your name:')
            total_amount = int(input('Enter a deposit amount:'))
            client_1= Client(name,total_amount)
            b.add_client(client_1)
            print('Account created successfully!Your account number is:{}'.format(client_1.account_number))
            #print('Choose an option:','\n','1.Open a new bank account','\n','2.Open an existing bank account','\n','3.Exit')
        elif number == 2:
            print('To access your account, please enter your credentials below','\n')
            name = input('Enter your name:')
            account_number = int(input('Enter your account number:'))
            c_authentication= b.authentication(name,account_number)
            if c_authentication:
                print('Welcome{}',format(client_1.name))
                for i in range(len(b.clients)):
                    if b.clients[i]['account_number']== account_number:
                        break
                while True:
                    print("""Choose an option:
                    1.Withdraw
                    2.Deposit
                    3.Balance
                    4.Exit""")
                    number1=input('Enter a number:')
                    if number == 1:
                        client_1.withdraw()
                    elif number == 2:
                        client_1.deposit()
                    elif number == 3:
                        client_1.balance()
                    else:
                        break
            else:
                print('Authentication failed!','\n','Reason: account is not found')
                    

            
