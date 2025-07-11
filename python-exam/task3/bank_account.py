# --- BankAccount Class Implementation
class BankAccount:
    """
    Represents a single bank account with basic operations
    - attribute: balance
    """

    def __init__(self, initial_balance=0.0):
        # constructor for the BankAccount class - initializes the account balance
        if initial_balance >= 0:
            self.balance = float(initial_balance)
        else:
            print("Warning: Initial balance cannot be negative. Setting to 0.0.")
            self.balance = 0.0

    def deposit(self, amount):
        # deposits a specified amount into the account
        if amount > 0:
            self.balance += float(amount)
            print(f"Successfully deposited: {amount:.2f}. New balance: {self.balance:.2f}.")
        else:
            print("Error: Deposit must be positive.")

    def withdraw(self, amount):
        # withdraws a specified amount from the account if funds are sufficient
        if amount <= 0:
            print(f"Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Successfully withdrew: {amount:.2f}. New balance: {self.balance:.2f}.")
        else:
            self.balance -= float(amount)
            print(f"Successfully withdrew: {amount:.2f}. New balance: {self.balance:.2f}.")
    
    def add_interest(self, rate):
        # adds interest to the current balance
        if rate >= 0:
            interest_earned = self.balance * float(rate)
            self.balance += interest_earned
            print(f"Interest added at rate {rate * 100:.2f}%. Interest earned: {interest_earned:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Error: Interest rate cannot be negative.")

    def get_balance(self):
        # returns the current balance of the account
        return self.balance

    def __str__(self):
        # returns a user-friendly string representation of the account's balance
        return f"Current Account Balance: {self.balance:.2f}"