from bank_account import BankAccount
class User:

    def __init__(self, name, email, balance = 0, int_rate = 0.025):
        self.name = name
        self.email = email
        self.bank_account = BankAccount(balance, int_rate)

    def make_withdrawal(self, amount):
        self.bank_account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.bank_account.balance}")
        return self
    
    def make_deposit(self, amount):
        self.bank_account.deposit(amount)
        return self

    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.make_deposit(amount)
            print(f"User: Money Transfered from {self.name} to {other_user.name}")
            return True
        print(f"User: Money Transfer failed")
        return False