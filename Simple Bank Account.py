class BankAccount:
    bank_name = "Generic Bank"  # Class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner  # Instance attribute
        self.balance = balance  # Instance attribute

    # Instance method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Instance method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    # Class method to change the bank name for all accounts
    @classmethod
    def set_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name updated to: {cls.bank_name}")

    # Static method to check if the deposit or withdrawal amount is valid
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    # Instance method to check balance
    def check_balance(self):
        return f"Balance: ${self.balance}"

# Create an instance of BankAccount
account = BankAccount("John Doe", 1000)

# Deposit money
account.deposit(500)
print(account.check_balance())  # Output: Balance: $1500

# Withdraw money
account.withdraw(300)
print(account.check_balance())  # Output: Balance: $1200

# Set the bank name (class method)
BankAccount.set_bank_name("MyBank")

# Check if an amount is valid
print(BankAccount.is_valid_amount(200))  # Output: True
