from bank import Bank
from client import Client

bank = Bank("ING")

print(f"Welcome to {bank.name}!")

available = True

while available:
    print('''
Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit

    ''')
    user_input = int(input())
    if user_input == 1:
        print("To create an account, please fill in the information below.")
        name = input("Name:")
        amount = int(input("Deposit amount:"))
        client = Client(name, amount)
        bank.add_client(client)
        print(f"Account created successfully! Your account number is: {client.account_number}")
    elif user_input == 2:
        print("To access your account, please enter your credentials below.")
        name = input("Name:")
        account_no = int(input("Account Number:"))
        curr_client = bank.authentication(name, account_no)
        if curr_client:
            authorized = True
            while authorized:
                print(f'''
                Welcome {curr_client.name}!

                Choose an option:

                    1. Withdraw
                    2. Deposit
                    3. Balance
                    4. Exit
                ''')
                curr_input = int(input("1, 2, 3, or 4:"))
                if curr_input == 1:
                    w_amount = int(input("Withdraw amount:"))
                    curr_client.withdraw(w_amount)
                elif curr_input == 2:
                    d_amount = int(input("Deposit amount:"))
                    curr_client.deposit(d_amount)
                elif curr_input == 3:
                    curr_client.balance()
                elif curr_input == 4:
                    authorized = False
                else:
                    print("Invalid input, please enter 1, 2, 3, or 4!")
    elif user_input == 3:
        available = False
    else:
        print('Input should be 1, 2, or 3!')
    