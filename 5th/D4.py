class bank:
    def __init__(self,original_sum,deposit_money,withdraw_money):
        self.deposit_money=deposit_money
        self.original_sum=original_sum
        self.withdraw_money=withdraw_money
    def deposit(self):
        new_sum=self.original_sum+self.deposit_money
        print(new_sum)
    def withdraw(self):
        new_sum=self.original_sum-self.withdraw_money
        print(new_sum)
bank(550,37,500)
        
        
        