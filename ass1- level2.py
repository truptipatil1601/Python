class BankAccount:
    # Constructor to initialize account details
    def __init__(self, account_number, account_holder_name, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Amount deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Amount withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    # Method to display account information
    def display_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Balance:", self.account_balance)
