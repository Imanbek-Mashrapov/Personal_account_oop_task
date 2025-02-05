from personal_account import PersonalAccount

if __name__ == '__main__':
    # Creating PersonalAccount object
    my_account = PersonalAccount(account_number=230121021, account_holder='Iman Mashrapov')

    # Depositing some money
    my_account.deposit(1000)
    my_account.deposit(200)

    # Withdrawing some money
    my_account.withdraw(700)
    my_account.withdraw(100)

    # Checking our balance
    print(f"The balance is {my_account.get_balance()}")
    print(my_account)
    print('\n')

    # Printing transaction history
    my_account.print_transaction_history()


