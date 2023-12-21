class Bank:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_account_number, entered_pin):
        if entered_account_number == self.account_number and entered_pin == self.pin:
            print("Login successful!")
            return True
        else:
            print("Invalid account number or pin. Login failed.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited successfully. Updated balance: {self.balance}")
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawn successfully. Updated balance: {self.balance}")
        else:
            print("Invalid amount or insufficient balance. Withdrawal failed.")

account1 = Bank(account_number="987654321", pin="9876", balance=6000)


entered_account_number = input("Enter account number: ")
entered_pin = input("Enter pin: ")

if account1.login(entered_account_number, entered_pin):
    # Deposit money
    deposit_amount = float(input("Enter amount to deposit: "))
    account1.deposit(deposit_amount)

    # Withdraw money
    withdrawal_amount = float(input("Enter amount to withdraw: "))
    account1.withdraw(withdrawal_amount)
