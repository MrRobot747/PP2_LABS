class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")

acc = Account("John", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  # Недостаточно средств
