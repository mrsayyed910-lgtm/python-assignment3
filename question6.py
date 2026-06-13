class BankAccount:
    def _init_(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance =", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance =", self.balance)

acc = BankAccount("Pradhyumn", 1000)

acc.deposit(500)
acc.withdraw(200)
