class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def withdraw(self,amount):
        if self.balance>=amount:

            self.balance-=amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance
    
#object
account=BankAccount("Owner", 200) 
account.deposit(100)
account.withdraw(500)
print("Balance", account.get_balance())       