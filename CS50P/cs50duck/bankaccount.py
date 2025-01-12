class BankAccount:
    def __init__(self, owner, balance=0):
        # Initialize the owner and balance attributes here
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Increase the balance by the amount deposited
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # Check if there is enough balance to withdraw
        if self.balance >= amount:
            # If so, decrease the balance by the amount withdrawn
            self.balance = self.balance - amount
            print("Withdrawal successful. New balance is", self.balance)
        else:
            # Otherwise, print a message indicating there are insufficient funds
            print("Insufficient funds")

    def get_balance(self, user):
        if user == self.owner:
            return self._balance
        else:
            raise PermissionError("Access denied")

bank_account = BankAccount("Jame")
bank_account.withdraw(10)
print(bank_account.balance)


