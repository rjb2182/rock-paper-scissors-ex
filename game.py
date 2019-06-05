# game.py

import random


print('Rock, Paper, Scissors, Shoot!')

#  Capture inputs

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes): ")

print("____________")
print("YOU CHOSE:", user_choice)
#  Validate inputs

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("Invalid selection, please try again...")
    exit()

#  Generate computer selection

print("Generating...")

computer_choice = random.choice(options)
print("___________")
print("The Computer Chose:", computer_choice)

#  DETERMINE THE WINNER

# rock beats scissors

# paper beats rock

# scissors beats paper

# same selection is a tie

if user_choice == computer_choice:
    print("TIE")

elif user_choice == 'rock' and computer_choice == "paper":
    print("THE WINNER IS PAPER")
    print("The computer won, sorry!")

elif user_choice == 'rock' and computer_choice == "scissors":
    print("THE WINNER IS ROCK")
    print("You Win!!  Yay you!")

elif user_choice == 'paper' and computer_choice == "scissors":
    print("THE WINNER IS SCISSORS")
    print("The computer won, sorry!")

elif user_choice == 'paper' and computer_choice == "rock":
    print("THE WINNER IS PAPER")
    print("You Win!!  Yay you!")

elif user_choice == 'scissors' and computer_choice == "paper":
    print("THE WINNER IS SCISSORS")
    print("You Win!!  Yay you!")

elif user_choice == 'scissors' and computer_choice == "rock":
    print("THE WINNER IS ROCK")
    print("The computer won, sorry!")












#  Display final outputs / outcomes

