class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal denied.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

# Main program
def main():
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(initial_balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
