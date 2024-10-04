# Hangman game in Python

import random
import os
from time import sleep

from unicodedata import category

from wordlist import fruits_words, animals_words, words

# dictionary of key:('tuple')
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
    for line in hangman_art[wrong_guesses]:
        print(f"    {line}")
    print("-*-*-*-*-*- ")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
        # answer = random.choice(words)
        word_category = ""
        while category:
            word_category = input("\n1. Fruits \n2. Animals \nChoose a category (1-2): ")
            if word_category == '1':
                word_category = "Fruits"
                answer = random.choice(fruits_words)
                break
            elif word_category == '2':
                word_category = "Animals"
                answer = random.choice(animals_words)
                break
            else:
                print("Invalid category")
                continue

        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        hangman_is_running = True

        while hangman_is_running:
            print("\n***********************")
            print(f"The category is {word_category}")
            print("***********************")
            display_man(wrong_guesses)
            display_hint(hint)
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input")
                continue

            if guess in guessed_letters:
                print(f"You already guessed the letter {guess.upper()}!")
                continue

            guessed_letters.add(guess)

            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
                os.system('cls')
            else:
                wrong_guesses += 1
                os.system('cls')

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("Congratulations! You won!")
                hangman_is_running = False
                sleep(5)
            elif wrong_guesses >= 6:
                display_man(wrong_guesses)
                print(f"The correct answer is\n")
                display_answer(answer)
                print("\nGame over! Sorry, you lose!")
                hangman_is_running = False
                sleep(5)


if __name__ == '__main__':
    main()