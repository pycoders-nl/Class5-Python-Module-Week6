# Class5-Python-Module-Week6

## 1. Bank Project

In this project you will have 3 files:

- bank.py
- client.py
- main.py

**bank.py**

- You will have class `Bank`. This bank will have instance variable `name` and class variable `clients` list. Initially this list will be empty.
- This class will have method `add_client` method which appends the client to list
- And lastly this class will have `authentication` method which takes `name` and `account_number` as parameters and authenticates the client

**client.py**
- You will have class `Client` inside this file.
- Class `Client` will have `account` dictionary as the class variable. This dictionary will keep following info: "account_number, name, total_amount"
- `__init__` method will initialize this variables, it will take `name` and `total_amount` as params and will assign a random 5 digit int to `account_number`
- Lastly this class will have `withdraw`, `deposit` and `balance` methods.

**main.py**
- This class initially will create a bank object with a name you choose
 and then will print the following menu (it should print this menu, until user says exit) [**hint:** use while loop]:
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

- And lastly, in the main menu, if user input is 3: close the program

## 1.2. UML

Draw Use Case and Class Diagrams for this project.

## 2. UML Class Diagram 

Consider the code in file [uml_class.py](https://drive.google.com/file/d/15NyCCB97LNMbXTQ71u0fVCYUXwfkSPfZ/view?usp=sharing). Draw the UML Class Diagram corresponding to the Python code. You may assume the code compiles, all imports are taken care of, and all classes reside in the same package.

## 3. UML Use Case Diagram

Draw the UML Use Case Diagram for the followig scenario:

```
As a lecturer at a university, I am able to manage my exams and register the grades. 
For both these actions, I should always login first with my credentials, followed by a confirmation via an SMS code. 
When I am registering new exam results, I must confirm this action again when my session is older than five minutes. 
When I want to manage my exam, I can choose to either change its date or room.
```

## Hackerrank Questions

1. sWAP cASE: https://www.hackerrank.com/challenges/swap-case/problem

2. String Split and Join: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

3. Mutations: https://www.hackerrank.com/challenges/python-mutations/problem

4. Text Wrap: https://www.hackerrank.com/challenges/text-wrap/problem
