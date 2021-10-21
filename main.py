from bank import Bank
from client import client
class main(Bank):
    bank=Bank("firdevs")
    def loop(self):
        while True:
            temp = input(f"""This is 's account:
    1) deposit
    2) witdraw
    3) get balance
""")
            if temp == '1':
                client.deposit()
            elif temp == '2':
                client.withdraw()
            elif temp == '3':
                client.balance()
            else:
                print("Please enter a valid option!")

a=main
