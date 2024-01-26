"""
Program: numberGuess.py
Chapter 3 example
1/3/2024

Standard number guessing game application. User will provide the range of numbers for the game. Program will prompt and guide the player until they get the correct number.
"""

import random
import time

# Input phase
smaller = int(input("Please, enter the smaller number >> "))

while smaller.isnumeric() != True:
    smaller = input("Sorry, please enter a small DIGIT >>")

smaller = int(smaller)

larger = int(input("Now, please enter the larger number >> "))

while larger.isnumeric() != True:
    larger = input("Sorry, please enter a large DIGIT >>")

larger = int(larger)

# Processing phase
magicNum = random.randint(smaller, larger)
print("Selecting your magic number...")
time.sleep(3)
# Variable to track the number of attempts for the game
count = 0
# Loop to keep the game going until the number is guessed
while True:
    userNumber = int(input("Enter your guess >> "))
    count += 1

    # Logic to determine the game outcome
    if userNumber < magicNum:
        print("Sorry, your guess was too SMALL!")
    elif userNumber > magicNum:
        print("Sorry, your guess was too LARGE!")
    else:
        print("Congratulations! You guessed it in", count, "tries!")
        break

# Output phase
input("Thank you for playing! Press ENTER to quit.")