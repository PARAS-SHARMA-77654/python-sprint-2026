
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")
    
    def show_balance(self):
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")
        
        
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")



def main():
    print("=== Savings Account System ===\n")
    
    
    name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: ₹"))
    
 
    account = SavingsAccount(name, initial_balance)
    
    print("\n--- Account Created Successfully ---")
    account.show_balance()
    
  
    while True:
        print("\n=== Banking Menu ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        
        elif choice == '3':
            account.show_balance()
        
        elif choice == '4':
            print("\n--- Final Account Summary ---")
            account.show_balance()
            print("\nThank you for banking with us!")
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()