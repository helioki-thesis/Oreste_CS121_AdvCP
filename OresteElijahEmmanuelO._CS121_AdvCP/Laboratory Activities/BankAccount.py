class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  
        self._balance = balance
    
    @property
    def account_number(self):
        return self._account_number  
    
    @property 
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        pass

    def display_type(self):
        pass
    
    def print_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Type: {self.display_type()}")
        print("-------------------------")
    
class CurrentAccount(BankAccount):
    overdraft_limit = -5000

    def withdraw(self, amount):
        if self._balance - amount >= self.overdraft_limit:
            self._balance -= amount
            return True
        return False
    
    def display_type(self):
        return "Current Account"
    
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def display_type(self):
        return "Savings Account"

if __name__ == "__main__":

    savings1 = SavingsAccount("SA123", 1200)
    savings2 = SavingsAccount("SA456", 5000)
    current1 = CurrentAccount("CA456", 0)
    current2 = CurrentAccount("CA789", 2000)
    
    savings1.deposit(324)
    savings1.withdraw(211)
    
    savings2.deposit(1005)
    savings2.withdraw(778)
    
    current1.withdraw(206)
    current1.deposit(536)
    current1.withdraw(4335) 
    
    current2.withdraw(2598)
    current2.deposit(1065)
    
    savings1.print_account_details()
    savings2.print_account_details()
    current1.print_account_details()
    current2.print_account_details()