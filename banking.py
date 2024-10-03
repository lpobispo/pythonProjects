# Simple banking program in Python

def show_balance(current_balance):
    print("**********************")
    print(f"Your balance is P{current_balance:.2f}")
    print("**********************")

def deposit():
    deposit_amt = float(input("Enter amount to deposit: "))

    if deposit_amt < 0:
        print("**********************")
        print("That is an invalid amount to be deposited.")
        print("**********************")
        return 0
    else:
        return deposit_amt


def withdraw(current_balance):
    withdraw_amt = float(input("Enter amount to be withdrawn: "))

    if withdraw_amt > current_balance:
        print("**********************")
        print("Insufficient balance")
        print("**********************")
        return 0
    elif withdraw_amt < 0:
        print("**********************")
        print("Amount should be greater than 0.")
        print("**********************")
        return 0
    else:
        return withdraw_amt

def main():
    current_balance = 0
    bank_is_running = True

    while bank_is_running:
        print("\n**********************")
        print("   Banking Program   ")
        print("**********************")

        print("1. Show balance")
        print("2. Make a deposit")
        print("3. Withdraw funds")
        print("4. Exit")
        print("**********************")
        user_choice = input("Enter a choice (1-4): ")

        if user_choice == '1':      # show balance
            show_balance(current_balance)
        elif user_choice == '2':    # deposit
            current_balance += deposit(current_balance)
        elif user_choice == '3':    # withdraw
            current_balance -= withdraw(current_balance)
        elif user_choice == '4':    # exit program
            print("**********************")
            print("Thank you for using XYZ Bank.")
            print("Have a great day!")
            print("**********************")
            bank_is_running = False
        else:
            print("**********************")
            print("Invalid option! Please try again.")
            print("**********************")

if __name__ == '__main__':
    main()