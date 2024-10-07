# Python slot machine
import random
from time import sleep


def spin_row():
    symbols = ['🍿', '🍟', '🍕', '🌭', '🍔']             # declaring the list of symbols

    return [random.choice(symbols) for _ in range(3)]     # iterate through the list 3 times and return
                                                          # a random symbol from the list

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:      # checks if all symbols are the same
        if row[0] == '🍿':
            return bet * 2
        elif row[0] == '🍟':
            return bet * 3
        elif row[0] == '🍕':
            return bet * 4
        elif row[0] == '🌭':
            return bet * 8
        elif row[0] == '🍔':
            return bet * 15
    return 0


def main():
    balance = int(input("Deposit amount to play: "))       # starting balance of the user

    print("\n******************************")
    print("Welcome to Python Slot Machine")
    print("   Symbols: 🍿 🍟 🍕 🌭 🍔   ")
    print("******************************")

    while balance > 0:
        print(f"\nYour current balance: P{balance}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():       # checks if bet is not a digit/number
            print("Please enter a valid amount")
            continue

        bet = int(bet)              # converting bet into int

        if bet > balance:           # checks if bet is greater than the current balance
            print("Insufficient funds")
            continue

        if bet <= 0:                # checks if bet is less than or equal to 0
            print("Bet must be greater than 0")
            continue

        balance -= bet              # if bet is valid, bet will be deducted to the current balance

        # row slot spinning
        row = spin_row()
        print("Spinning..\n")
        sleep(0.5)                  # loading effect
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:              # checks if the user won
            print(f"You won P{payout}!")
        else:
            print("Sorry you lost this round")

        balance += payout

        keep_playing = input("Do you want to play again? (Y/N): ").upper() # ask the user to play again

        if balance == 0 and keep_playing == "Y":            # checks if balance is 0 and player still wants to play
            print("Sorry, you don't have enough funds")
            break
        if keep_playing != "Y":
            break                   # exit the program if the input is not 'Y'

    print(f"Thank you for playing! Your final balance is P{balance:.2f}")
    sleep(3)


if __name__ == '__main__':
    main()