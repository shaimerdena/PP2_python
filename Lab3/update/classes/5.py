class Account:
    def __init__(self, owner, balance):
        self.name = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print(self.name, ",you have", self.balance, "in your bank")
    def withdraw(self, money):
        if (self.balance - money) < 0:
            print("Insufficient funds. Try again.")
        else:
            self.balance -= money
            print(self.name, ", you have", self.balance, "in your bank")

name = input()
balance = float(input())
account = Account(name, balance)

account.deposit(100)
account.withdraw(50)
account.deposit(1000)
account.withdraw(5000)

