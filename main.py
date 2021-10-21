from client import Client  #Client and Bank Classes are imported.
from bank import Bank

bank=Bank("Asya") # i give a bank name to my bank object
print(f"Welcome to International {bank.name} Bank")

while True: # I used while to return the code until user press 3 button
    print("""Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit""")

    choice=int(input("1,2,3 : "))
    if choice==1: #If choice is one i crreated a new client
        print("To create an account, please fill in the information below.")
        client=Client(input("Name: "),float(input("Deposit amount: ")))
        bank.add_client(client)
        client_account=client.account["account_number"]
        print(f"Account created succesfully. Your account number is {client_account}")

    elif choice==2: # if choise is 2 . The name and bank account are controlled if they are true.
        try:
            print("To access your account, please enter your credentials below.")
            name=input("name: ")
            account_number=int(input("enter your account number:"))
        except Exception:
            print("""Authentication failed! 
            Reason: account not found""" )

        current_client=bank.authentication(name,account_number)
        if current_client:  # If they are true the code continues with the other section
            print("Welcome {}!".format(current_client.account["name"]))

        
            while True: # I used again while loop
                print("""Choose an option:

    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit""")
                choice2=int(input("1,2,3,4 : "))
                if choice2==1: # if choice2 is 1 , I calculated the balance with the withdraw method.
                    
                    
                        withdraw=int(input("Withdraw amount: "))

                        current_client.withdraw(withdraw)
                        
                elif choice2==2: # If the choice2 is 2 < i calculated the balance with the deposit method.
                    deposit=int(input("Deposit amount: "))
                    current_client.deposit(deposit)
                    
                elif choice2==3:  #If choice2 is 3 , The balance is showed by the user
                    current_client.balance()
                
                
                elif choice2==4: # If the choice2 , the loop will be finished. And will turn the main menu.
                    break
    elif choice==3: #If the user press 3 the program will be finished.
        print("Thank you very much to be a client of us. Have a nice day")
        break

        


