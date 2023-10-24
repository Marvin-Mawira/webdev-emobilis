class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Create instances of the BankAccount class
account1 = BankAccount("Alice")
account2 = BankAccount("Bob", 1000)

# Interact with the bank accounts
account1.display_account_info()
account1.deposit(500)
account1.withdraw(200)
account1.display_account_info()

account2.display_account_info()
account2.deposit(1000)
account2.withdraw(2000)
account2.display_account_info()
