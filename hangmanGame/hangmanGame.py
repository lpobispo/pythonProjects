# Hangman game in Python

import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

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
        print(f"\t{line}")
    print("-*-*-*-*-*- ")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
        answer = random.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        hangman_is_running = True

        while hangman_is_running:
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
            else:
                wrong_guesses += 1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(hint)
                print("You win!")
                hangman_is_running = False
            elif wrong_guesses >= 6:
                display_man(wrong_guesses)
                display_answer(hint)
                print("You lose!")
                hangman_is_running = False

if __name__ == '__main__':
    main()