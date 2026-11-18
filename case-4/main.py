# Project 04: ATM Transaction Sequence Simulation
balance = 5000.00

print("WELCOME TO THE ATM")
while True:
    print("\n1. Balance Enquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Available balance: Rs.", round(balance, 2))
    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))
        if amount > 0:
            balance = balance + amount
            print("Deposit successful.")
            print("New balance: Rs.", round(balance, 2))
        else:
            print("Amount must be greater than zero.")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance = balance - amount
            print("Please collect your cash.")
            print("New balance: Rs.", round(balance, 2))
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Select 1, 2, 3, or 4.")
