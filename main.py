from client import Client
from bank import Bank



int_bank=Bank("International")
while True:  
      option =input("""Welcome to International Bank
    Choose an option:
    1. Open new bank account
    2. Open existing bank account
    3. Exit \n Enter :""")
      if option == "1":
          name=input("Name :")
          total_amount=int(input("Amount :"))
          client=Client(name,total_amount)
          int_bank.add_client(client)
          print ("Acoount of %s,%s has been added"%(name,total_amount))
          
      elif option=="2":
          print("To access your account, please enter your credentials below.")
          acc_No=input("Account No : ")
          name=input("Name : ")
          if int_bank.authentication(name,acc_No):
            
           while True:
                choice=input( """
Welcome %s !
Choose an option:
  1. Withdraw
  2. Deposit
  3. Balance
  4. Exit 
"""%(name))
                if choice=="1":
                    amount=int(input("Withdraw Amount : "))
                    for i in Bank.clients:
                       i.withdraw(amount)
                elif choice=="2":
                    amount=int(input("Deposit Amount : "))
                    for i in Bank.clients:
                       i.deposit(amount)
                    
                elif choice=="3":
                  for i in Bank.clients:
                       i.balance()
                elif choice=="4":
                     break
               
      elif (option=="3"):
        print("See you soon...")
        break


