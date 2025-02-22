from amount import Amount


class PersonalAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__transactions = []

    # A method to deposit money into the account.
    def deposit(self, amount):
        if amount < 0:
            print(f"Sorry you can not deposit negative amount ({amount})")
        else:
            operation = Amount(amount, transaction_type='DEPOSIT')
            self.__transactions.append(operation)
            self.__balance = self.__balance + amount

    # A method to withdraw money from the account.
    def withdraw(self, amount):
        if self.__balance < amount:
            print(f"Amount exceeds the current balance, all balance ({self.__balance}) is withdrawn")
            amount = self.__balance
            self.__balance = self.__balance - amount
            operation = Amount(amount, transaction_type='WITHDRAW')
            self.__transactions.append(operation)
        else:
            operation = Amount(amount, transaction_type='WITHDRAW')
            self.__transactions.append(operation)
            self.__balance = self.__balance - amount

    # A method to print the transaction history of the account
    def print_transaction_history(self):
        if not self.__transactions:
            print("No transactions have been yet")
        else:
            for transact in self.__transactions:
                print(transact)

    # A method to retrieve the current balance of the account.
    def get_balance(self):
        return self.__balance

    # A method to retrieve the account number.
    def get_account_number(self):
        return self.__account_number

    # A method to set the account number.
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # A method to retrieve the account holder's name.
    def get_account_holder(self):
        return self.__account_holder

    # A method to set the account holder's name.
    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    # Provides a string representation of the object
    def __str__(self):
        return f"Account number: {self.__account_number}, Account holder: {self.__account_holder}, Balance: {self.__balance}"

    # Performs the same operation as the deposit(self, amount)
    def __add__(self, amount):
        self.deposit(amount)

    # Performs the same operation as the withdraw(self, amount)
    def __sub__(self, amount):
        self.withdraw(amount)
