class BankAccount:
    
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return "Your bank account balance {} and here is your interest rate {}%.".format(self.balance, self.interest_rate)

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return self.balance

    def withdraw_money(self, deposit_amount):
        self.balance -= deposit_amount
        return "You just made a withdrawal! Your new balance is ${:.2f}.".format(self.balance)

    def gain_interest(self):
        self.balance = self.balance + self.balance * self.interest_rate
        return "You just earned interest! Your new balance is ${:.2f}.".format(self.balance)

my_acc = BankAccount(10000, 10)
print(my_acc.deposit(1000))
print(my_acc.withdraw_money(150))
print(my_acc.gain_interest())