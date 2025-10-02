balance = 1000
withdrawal = 0

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"Your balance is {balance}")

    elif choice == 2:
        amount = int(input("Enter amount: "))
        balance += amount
        print(f"You deposited {amount} to {balance}")

    elif choice == 3:
        if withdrawal >= 3:
            print("You reached the daily withdrawal limit.")
        else:
            balance -= amount
            withdrawal += 1
            print(f"You withdrew {amount}. New balance is {balance}")

    elif choice == 4:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice. Please try again.")