# Personal Account Management

## Objective
#### This project is a Python program for managing a personal bank account. It demonstrates the use of Object-Oriented Programming (OOP) concepts such as classes, objects, methods, and encapsulation.

## Features
- #### Create and manage a personal account
- #### Deposit and withdraw money
- #### Track transaction history
- #### Check account balance

## Classes
### 1. Amount
#### This class represents a transaction, including:

- #### amount: The transaction amount

- #### transaction_type: The type of transaction (DEPOSIT or WITHDRAW)

- #### timestamp: The date and time of the transaction

### Methods:

#### __str__(): Returns a string representation of the transaction

###  2. PersonalAccount
#### This class manages a bank account, including deposits, withdrawals, and transaction history.

### Attributes:

- #### __account_number: Unique account identifier

- #### __account_holder: Name of the account holder

- #### __balance: Current account balance

- #### __transactions: List of all transactions

### Methods:

- #### deposit(amount): Deposits money into the account

- #### withdraw(amount): Withdraws money if sufficient funds are available

- #### print_transaction_history(): Prints all transactions

- #### get_balance(): Returns the current balance

- #### get_account_number(): Retrieves account number

- #### set_account_number(account_number): Updates the account number

- #### get_account_holder(): Retrieves account holder’s name

- #### set_account_holder(account_holder): Updates the account holder’s name

- #### __str__(): Returns a string representation of the account

- #### __add__(amount): Overloads + to perform a deposit

- #### __sub__(amount): Overloads - to perform a withdrawal

## UML Class Diagram
![personal_account_uml.png](personal_account_uml.png)[personal_account_uml.png]

## Test Cases
#### Here are some test cases to verify the functionality:

### Test Case 1: Deposit Money

#### Steps:

- Create an account
- Deposit 1000
- Deposit 200
- Check balance

#### Expected Output:
"The balance is 1200.0"

### Test Case 2: Withdraw Money

#### Steps:

- Withdraw 700
- Withdraw 100
- Check balance

#### Expected Output:
"The balance is 400.0"

### Test Case 3: Withdraw More Than Balance

#### Steps:

- Withdraw 500 (exceeds balance)

#### Expected Output:

"Amount exceeds the current balance, all balance (400.0) is withdrawn
The balance is 0.0"

### Test Case 4: Transaction History

#### Expected Output:

"Amount: 1000, Time: ..., Transaction_type: DEPOSIT

Amount: 200, Time: ..., Transaction_type: DEPOSIT

Amount: 700, Time: ..., Transaction_type: WITHDRAW

Amount: 100, Time: ..., Transaction_type: WITHDRAW

Amount: 400, Time: ..., Transaction_type: WITHDRAW"

