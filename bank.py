# python progran to demonstrate bank operations
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = 0.0
        self.date_of_opening = date_of_opening or datetime.now().strftime("%Y-%m-%d")
    # method to do  deposit operations
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
        # method to perform  withraw operations
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance for {self.customer_name}: ${self.balance:.2f}")
    # metthod to create customer details
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: ${self.balance:.2f}")

def main():
    # Create a new bank account
    account = BankAccount("89112730", "David W Soita")
    print(f"Created new account for {account.customer_name} with account number {account.account_number}")

    # Perform some operations
    account.customer_details()
    account.deposit(1000)
    account.check_balance()
    account.withdraw(500)
    account.check_balance()
    account.withdraw(300)
    account.check_balance()
    account.customer_details()

if __name__ == "__main__":
    main()
