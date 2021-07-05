class bank:
    def __init__(self,original_sum):
        self.original_sum=original_sum
    def deposit(self,deposit_money):
        self.deposit_money=deposit_money
        new_sum=self.original_sum+self.deposit_money
        print(new_sum)
    def withdraw(self,withdraw_money):
        self.withdraw_money=withdraw_money
        new_sum=self.original_sum-self.withdraw_money
        print(new_sum)
a=bank(550)
a.withdraw(300)
a.deposit(300)
        
        
        