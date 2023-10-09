class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

# Create a bank account object
account = BankAccount("12345", 1000)

# Perform transactions using the interface
account.deposit(500)
account.withdraw(200)

# Access balance through the interface
print("Current balance:", account.get_balance())
