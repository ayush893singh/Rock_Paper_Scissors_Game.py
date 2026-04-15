# Rock Paper Scissors Game

## About
This is a simple Python-based game where the user plays **Rock–Paper–Scissors** against the computer.
The computer randomly selects one option, and the winner is decided based on the rules:

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock

## Technologies Used
* **Python** – Core programming language
* **random module** – Used to let the computer choose randomly
* **Input/Output functions** – `input()` and `print()` for user interaction

## How It Works
1. The program displays game rules.
2. The user enters a choice: `rock`, `paper`, or `scissors`.
3. The computer randomly selects one option.
4. The program compares both choices:
   * Same choice → It's a tie
   * Otherwise → Winner is decided using conditions
5. Result is displayed on the screen.

## How to Run

1. Install Python on your system
2. Copy the code into a file named `Rock_Paper_Scissors_Game.py`
3. Open terminal / command prompt
4. Run the program:

   ```
   python game.py
   ```

## Code
```
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
```

## Output 
```
----- Welcome to GAME -----

Rock vs Paper = Paper
Paper vs Scissors = Scissors
Scissors vs Rock = Rock

Enter your choice (rock/paper/scissors): paper
Computer chose: rock
You win!
```

## Author

**Ayush Singh**
GitHub: https://github.com/ayush893singh
