"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""
class BankAccount:
     def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

     def deposit(self, amount):
        self.balance += amount

     def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

     def get_balance(self):
        return self.balance

acc1 = BankAccount("Gotom", 100000)
acc2= BankAccount ("Nenny",50000)
acc1.deposit(5000)
acc2.withdraw(2000)
print(acc1.get_balance())
print(acc2.get_balance())