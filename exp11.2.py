import json
import os

# Custom exceptions
class InsufficientFundsError(Exception):
    """Exception raised for insufficient funds during withdrawal."""
    pass

class InvalidAmountError(Exception):
    """Exception raised for invalid deposit or withdrawal amounts."""
    pass

# Base class for Account
class Account:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}")

    def display_info(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance:.2f}"

# Subclass for Savings Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print(f"Applied interest: {interest}. New balance: {self.balance:.2f}")

# Subclass for Current Account
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)

# Function to save account data to a file
def save_accounts(accounts, filename='accounts.json'):
    with open(filename, 'w') as file:
        json.dump([account.__dict__ for account in accounts], file)

# Function to load account data from a file
def load_accounts(filename='accounts.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        account_data = json.load(file)
        accounts = []
        for data in account_data:
            if 'interest_rate' in data:
                account = SavingsAccount(data['account_number'], data['account_holder'], data['interest_rate'])
            else:
                account = CurrentAccount(data['account_number'], data['account_holder'])
            account.balance = data['balance']
            accounts.append(account)
        return accounts

# Main function to demonstrate the banking system
def main():
    accounts = load_accounts()

    # Creating some accounts
    try:
        savings_account = SavingsAccount("S123", "Alice", 3.5)
        savings_account.deposit(1000)
        savings_account.withdraw(200)
        savings_account.apply_interest()
        accounts.append(savings_account)

        current_account = CurrentAccount("C123", "Bob")
        current_account.deposit(500)
        current_account.withdraw(100)
        accounts.append(current_account)

        # Display account information
        for account in accounts:
            print(account.display_info())
            print("-" * 40)

    except (InsufficientFundsError, InvalidAmountError) as e:
        print(f"Error: {e}")

    # Save accounts to file
    save_accounts(accounts)

if __name__ == "__main__":
    main()
