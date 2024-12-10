class Bank:
    def __init__(self):
        self.closingBal = 0

    def display(self):
        while True:
            print("\nEnter Your Options:")
            print("1 for Deposit")
            print("2 for Withdraw")
            print("3 to Exit")
            
            getOption = input("Choose an option: ")

            if getOption == "1":
                self.deposit()
            elif getOption == "2":
                self.withdraw()
            elif getOption == "3":
                print("Thanks for visiting our bank.")
                break
            else:
                print("Invalid option. Please try again.")

    def deposit(self):
        try:
            depositAmount = int(input("Enter your deposit amount: "))
            self.closingBal += depositAmount
            print(f"Amount deposited successfully. Current balance: {self.closingBal}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        try:
            withdrawAmount = int(input("Enter your withdraw amount: "))
            if self.closingBal >= withdrawAmount:
                self.closingBal -= withdrawAmount
                print(f"Withdrawal successful. Current balance: {self.closingBal}")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Create an instance of the Bank class and start the application
bankObj = Bank()
bankObj.display()
