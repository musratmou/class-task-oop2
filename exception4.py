class InsufficientBalance(Exception):
    def __init__(self, message="Insufficient balance to withdraw the amount"):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance(f"Cannot withdraw {amount}. Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

# Example usage
try:
    account = BankAccount(1000)
    account.withdraw(1500)
except InsufficientBalance as e:
    print(f"Error: {e}")
