# Python Rock Paper Scissor game
# random module

import random

jakNpoy = ("rock", "paper", "scissors")
is_playing = True

print()
print("Welcome to Python Rock Paper Scissors game")
print("Select R for Rock, P for Paper, S for Scissors")
print("---------------------------------------")
print()

while is_playing:

    player = None
    computer = random.choice(jakNpoy)

    while player not in jakNpoy:
        player = input("Select a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    else:
        print("You lose!")
    print()
    if not input("Play again? (y/n): ").lower() == "y":
        is_playing = False

print("------ Thanks for playing! ------")









# while is_running:
#     guess = input("Select your guess: ").lower()
#     print()
#     if guess.isalpha():
#         if guess != "r":
#             print(f"{guess.upper()} is invalid!")
#             print(f"Please select R for Rock, P for Paper, S for Scissors")
#             print()
#         elif guess != "p":
#             print(f"{guess.upper()} is invalid!")
#             print(f"Please select R for Rock, P for Paper, S for Scissors")
#             print()
#         elif guess != "s":
#             print(f"{guess.upper()} is invalid!")
#             print(f"Please select R for Rock, P for Paper, S for Scissors")
#             print()
#         else:
#             if guess == "r" and answer == "rock":
#                 print("It's a tie!")
#                 break
#             elif guess == "p" and answer == "paper":
#                 print("It's a tie!")
#                 break
#             elif guess == "s" and answer == "scissors":
#                 print("It's a tie!")
#                 break
#
#     else:
#         print(f"{guess.upper()} is invalid!")
#         print(f"Please select R for Rock, P for Paper, S for Scissors")
#         print()