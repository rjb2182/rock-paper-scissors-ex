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

#  Determine the winner



#  Display final outputs / outcomes

