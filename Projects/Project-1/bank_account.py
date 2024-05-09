class Bank_Account:
    def __init__(self,initial_amount,bank_acc):
        self.Balance=initial_amount
        self.Bank_Name=bank_acc
        print("Account",self.Bank_Name,"created")
        print("Balance=",self.Balance)
        print()
    def getbalance(self):
        print("Account",self.Bank_Name,"Balance","=",self.Balance)
        print()

    def deposit(self,amount):
        self.Balance=self.Balance+amount
        print("Deposit Created")
        self.getbalance()
    def withdraw(self,amount):
        if(self.Balance<amount):
            print("Withdrawal not possible")
        else:
            self.Balance-=amount
            print("Amount Withdraw:",amount)
            self.getbalance()

