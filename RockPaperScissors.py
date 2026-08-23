python
import random

print("\n----- Welcome to GAME -----\n")
print("Rock vs Paper = Paper")
print("Paper vs Scissors = Scissors")
print("Scissors vs Rock = Rock\n")

choices = ["rock", "paper", "scissors"]

user = input("Enter your choice (rock/paper/scissors): ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")

elif user == "rock":
    if computer == "paper":
        print("Computer wins!")
    else:
        print("You win!")

elif user == "paper":
    if computer == "scissors":
        print("Computer wins!")
    else:
        print("You win!")

elif user == "scissors":
    if computer == "rock":
        print("Computer wins!")
    else:
        print("You win!")

else:
    print("Invalid input!")