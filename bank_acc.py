class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit Successful! New Balance: {self.balance}"
        else:
            return "Invalid deposit amount"
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount 
            return f"Withdrawal successful! New Balance: {self.balance}"
        else: 
            return "Insufficient funds!"
        
    def get_balance(self):
        return f"Account Balance: {self.balance}"
    
    
# Create a bank account for John with an initial balance of 1000
john_account = BankAccount("John", 1000)

# Check balance 
print("The balance in your account is: ", john_account.get_balance())

# Deposit money
print(john_account.deposit(500))

#check balance again
print("The balance in your account is: ", john_account.get_balance())

# Withdraw money
print(john_account.withdraw(200))

# Withdraw more money then balance
print(john_account.withdraw(2000))
