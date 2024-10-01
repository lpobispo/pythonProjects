# Python number guessing game
# random module

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("---- Welcome to Python Number Guessing Game ----")
print(f"Select a number between {lowest_num} and {highest_num}")
print("------------------------------------------------")

while is_running:
    # user input
    guess = input("Enter your guess: ")

    if guess.isdigit():         # checks if the user's guess is a number/digit
        guess = int(guess)      # convert the guess into integer
        guesses += 1            # guesses variable will increment by one for every correct guess
        if guess < lowest_num or guess > highest_num:   # checks if the user input is out of range
            print("Your guess is out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
            print()
        elif guess < answer:                            # checks if user's guess is less than the answer
            print("Your guess is too low. Try again.")
            print()
        elif guess > answer:                            # checks if user's guess is higher than the answer
            print("Your guess is too high. Try again.")
            print()
        else:                                           # checks if the user's guess is equal to the answer
            print(f"Correct! The correct number is {answer}")
            print(f"You have a total of {guesses} guesses.")
            is_running = False
    else:       # user's input is not a number/digit.
        print("Your guess is invalid!")
        print(f"Please select a number between {lowest_num} and {highest_num}")
        print()