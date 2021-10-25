'''**main.py**
- This class initially will create a bank object with a name you choose and then will print the following menu (it should print this menu, until user says exit) [**hint:** use while loop]:
```
Welcome to International Bank!

Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
```
Then it will take the user input: 
- If it is 1, create an account
First ask the name and then the deposit amount to user:
```
To create an account, please fill in the information below.
Name: 
Deposit amount: 
```
After this, it creates the account and prints the menu again
```
Account created successfully! Your account number is:  88194

Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
```
- If it is 2, asks following info
```
To access your account, please enter your credentials below.
Name:
Account Number:
```
First asks name and then account number. 
If credentials are wrong, print following, and then print the menu again:
```
Authentication failed!
Reason: account not found.
```
If credentials are correct, prints the following menu:
```
Authentication successful!

Welcome irem!

Choose an option:

    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit
```
And according to user input you can withdraw, deposit money. Or see the current balance. 
If input is 1, asks for withdraw amount:
```
Withdraw amount:
```
And according to user input witdraws the amout and prints the menu again.
```
The sum of 100 has been withdrawn from your account balance.

Your current account balance is: 900
```
If input is 2, asks for deposit amount:
```
Deposit amount:
```
And according to user input, in this case 300. Prints following:
```

The sum of 300 has been added to your account balance.

Your current account balance is: 1200
```

If input is 3, shows the current balance:

```
Your current account balance is: 1200

```
If input is 4, it goes back to other menu.

- And lastly, in the main menu, if user input is 3: close the program'''

from client import Client
from bank import Bank

international_bank = Bank("International")
while True:
    choice = input("Welcome to International Bank!\nChoose an option:\n1. Open new bank accountn\n2. Open existing bank accountn\n3. Exit")
    if (choice == "1"):
        print("To create an account, please fill in the information below.\nName\nDeposit amount:")
        name =input("Name:")
        total_amount=int(input("Deposit amount:"))
        client = Client(name, total_amount)
        international_bank.add_client(client)
    elif (choice == "2"):
        print("To access your account, please enter your credentials below.")
        name =input("Name:")
        account_number = int(input("Account Number:"))
        '''if not international_bank.authentication(name, account_number=):
            print("Authentication failed!\nReason: account not found.")'''
        if international_bank.authentication(name, account_number) :
            print("Authentication successful!\nWelcome {name}!")
            choice1 = input("Choose an option:\n1. Withdraw\n2. Deposit\n3. Balance\n4. Exit")
            if choice1 == "1":
                withdraw = int(input("Withdraw amount:"))
                for i in Bank.clients:
                    if i.name == name and i.account_number == account_number :
                        i.withdraw(withdraw)
            elif choice1=="2":
                Deposit_amount:int(input("Deposit amount:"))
                for i in Bank.clients:
                    if i.name == name and i.account_number == account_number : 
                        i.deposit(Deposit_amount)
                print("The sum of {Deposit_amount} has been added to your account balance\nYour current account balance is: {Deposit_amount} + {balance}")
            elif choice1=="3":
                for i in Bank.clients:
                    if i.name == name and i.account_number == account_number : 
                        print(i.balance())
            elif choice1=="4":
                break
            else : 
                print("Error")
    elif choice == "3" :
        break
    else:
        print("error")
