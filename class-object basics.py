class Account():
    def __init__(self, onwer, balance = 0):
        self.onwer = onwer
        self.balance = balance
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print('You have deposited {}$ in your account'.format(deposit_amount))

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance = self.balance - withdraw_amount
            print('You have withdraw {}$ from your account'.format(withdraw_amount))
        else:
            print('Sorry! You have not sufficient balance to withdraw. Your account balance is {}'.format(self.balance))    


acc1 = Account('Hamid', 2000)
acc1.withdraw(2000)
print(acc1.balance)