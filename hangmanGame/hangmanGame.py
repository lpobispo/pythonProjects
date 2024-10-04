# Hangman game in Python

import random           # to random answer from wordlist.py
import os               # to clear console screen
from time import sleep  # to add delay before closing program

from wordlist import fruits_words, animals_words

# dictionary of key: ('tuple')
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "),
               3: (" O ",
                   "/| ",
                   "   "),
               4: (" O ",
                   "/|\\",
                   "   "),
               5: (" O ",
                   "/|\\",
                   "/  "),
               6: (" O ",
                   "/|\\",
                   "/ \\")}


def display_man(wrong_guesses):
    print("-*-*-*-*-*-")
    for line in hangman_art[wrong_guesses]:     # iterate each line in hangman_art dictionary and print based on the pass parameters
        print(f"    {line}")
    print("-*-*-*-*-*- ")


def display_hint(hint):
    print(" ".join(hint))                       # iterates through answer then joining _ and a space

def display_answer(answer):
    print(" ".join(answer))                     # iterates through answer then joining each letters from answer and a space
    pass
def main():
        # answer = random.choice(words)
        word_category = ""                      # initialize variable
        choosing_category = True                # initialize to true

        # while choosing_category is true, repeat the while loop
        while choosing_category:
            word_category = input("\n1. Fruits \n2. Animals \nChoose a category (1-2): ")
            if word_category == '1':
                word_category = "Fruits"
                answer = random.choice(fruits_words)    # answer will choose words from the set of fruits
                choosing_category = False           # choosing_category turns to false to exit the while loop
            elif word_category == '2':
                word_category = "Animals"
                answer = random.choice(animals_words)   # answer will choose words from the set of animals
                choosing_category = False           # choosing_category turns to false to exit the while loop
            else:                                   # if category is invalid (not 1 or 2), continue to loop
                print("Invalid category")
                continue

        hint = ["_"] * len(answer)                  # _ will substitute each letter multiplied by the length of the answer
        wrong_guesses = 0                           # initialized variable. Technically start the hangman_art dict to key 0
        guessed_letters = set()                     # initialized to empy set
        hangman_is_running = True                   # initialized to True

        while hangman_is_running:
            print("\n***********************")
            print(f"The category is {word_category}")
            print("***********************")
            display_man(wrong_guesses)
            display_hint(hint)
            guess = input("Guess a letter: ").lower()       # user will guess a single letter


            if len(guess) != 1 or not guess.isalpha():      # checks if guess is more than 1 letter or guess is not a letter
                os.system('cls')                            # to clear console screen
                print("Invalid input")
                continue

            if guess in guessed_letters:                    # checks if guessed letter is already stored in the guessed_letters set
                os.system('cls')                            # to clear console screen
                print(f"You already guessed the letter {guess.upper()}!")
                continue
            guessed_letters.add(guess)                      # stores the guessed letter to the set


            if guess in answer:                             # checks if guessed letter is in answer
                for i in range(len(answer)):                # iterate i through the range of length of answer
                    if answer[i] == guess:                  # if index of answer is equal to guessed letter
                        hint[i] = guess                     # then index of hint is set to guessed letter
                os.system('cls')                            # to clear console screen
            else:
                wrong_guesses += 1                          # if guessed letter is not within the answer wrong_guesses incremented by 1
                os.system('cls')                            # to clear console screen

            if "_" not in hint:                             # checks if hint no longer have _ (meaning all correct letters are guessed)
                display_man(wrong_guesses)
                display_answer(answer)
                print("Congratulations! You won!")
                hangman_is_running = False                  # set to false to exit the loop
                sleep(5)                                    # 5 seconds delay before closing the program
            elif wrong_guesses >= 6:
                display_man(wrong_guesses)
                print(f"The correct answer is\n")
                display_answer(answer)
                print("\nGame over! Sorry, you lose!")
                hangman_is_running = False                  # set to false to exit the loop
                sleep(5)                                    # 5 seconds delay before closing the program


if __name__ == '__main__':
    main()