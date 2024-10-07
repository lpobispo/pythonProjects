# Python Rock Paper Scissor game
# random module

import random
from time import sleep

jakNpoy = ("rock", "paper", "scissors")
is_playing = True

print()
print("Welcome to Python Rock Paper Scissors game")
print("---------------------------------------")
print()

while is_playing:

    player = None
    computer = random.choice(jakNpoy)

    while player not in jakNpoy:
        player = input("Select a choice (rock, paper, scissors): ")
        if player != 'rock' and player != 'paper' and player != 'scissors':
            print("Invalid input!")
            continue

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
sleep(3)