# Bank Account Balance Program

balance = float(input("Enter starting balance: "))

while balance > 0:

    print("\nCurrent Balance:", balance)

    print("1. Deposit Money")
    print("2. Withdraw Money")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":

        deposit = float(input("Enter amount to deposit: "))
        balance = balance + deposit

        print("Deposit successful.")

    elif choice == "2":

        withdraw = float(input("Enter amount to withdraw: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    else:
        print("Invalid choice.")

    print("Updated Balance:", balance)

print("\nBalance is now zero.")
print("Account session ended.")