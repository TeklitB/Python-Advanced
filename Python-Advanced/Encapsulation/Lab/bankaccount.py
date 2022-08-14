class AccountError(Exception):
    pass

class SingleBankAccount:
    def __init__(self, acc_num):
        self.__account_number = acc_num
        self.__account_balance = 0.0
    
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def account_balance(self):
        return self.__account_balance
    
    @account_number.setter
    def account_number(self, acnum):
        raise AccountError("You are not allowed to modify account number.")
    
    @account_balance.setter
    def account_balance(self, balance):
        if balance < 0.0:
            raise AccountError("Balance cannot be negative.")
        
        self.__account_balance = balance
    
    @account_number.deleter
    def account_number(self):
        if self.__account_balance <= 0:
            print(f"Since the balance is {self.__account_balance}, the account is deleted.")
            self.__account_number = None
            self.__account_balance = None
        
        else:
            raise AccountError("If balance is not zero, account cannot be deleted.")

    def deposite(self, amount):
        if amount < 0.0:
            raise AccountError("The amount to deposite cannot be negative.")
        
        if abs(amount - 100.00) > 0.001:
            print(f"You are depositing more than 100 ({amount})")
        
        self.__account_balance += amount
    
    def withdraw(self, amount):
        if amount < 0.0:
            raise AccountError("The amount to withdraw cannot be negative.")
        
        if abs(amount - 100.00) > 0.001:
            print(f"You are withdrawing more than 100 (i.e. {amount})")
        
        self.__account_balance -= amount   


bn = SingleBankAccount(123)
bn.account_balance = 1000

try:
    bn.account_balance = -200
except AccountError as ex:
    print(f"You are trying to set negative balance. {ex}")

try:
    bn.account_number = 12345
except AccountError as ex:
    print(f"You are trying to modify the account number. {ex}")

bn.deposite(1000.000)

try:
    del bn.account_number
except AccountError as ex:
    print(f"You are trying to delete an acount in which its balance is not zero. {ex}")

