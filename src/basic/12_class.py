class BankAccount(object):
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Amount cannot be less ZERO')
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            raise ValueError('Amount cannot be less ZERO')
    
    def overdrawn(self) :
        return self.balance < 0

my_account = BankAccount(15)
my_account.withdraw(50)

print (my_account.balance, my_account.overdrawn())