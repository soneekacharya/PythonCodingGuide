""" There is a savings account and a checking account class. The checking account inherits the savings account as both have 
the same functionality and the checking account allows overdrafts (allow processing transactions even if there 
is not sufficient balance). Redesign this program to follow the Liskov Substitution Principle (LSP) principle which
represents that “objects should be replaceable by their subtypes without altering
how the program works”. """

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")

class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    #Performing bank actions on saving account
    perform_bank_actions(savings_account)

    #Performing bank actions on checking account
    perform_bank_actions(checking_account)
