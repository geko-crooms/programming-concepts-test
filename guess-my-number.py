"""
Guess my number game.
"""

import random

my_number = random.randrange(100)  # Picks a random number between 0 and 99.
attempts = 0
guess = int(input("Guess my number! It is from 0 to 99. You have 5 tries. "))

### YOUR CODE HERE


# Use the following lines
        print("Too low")
    print("Out of tries ― the number was ")
    print("You got it!")
    attempts += 1
else:
    guess = int(input("Guess my number! "))
while attempts < 5 and guess != my_number:
        print("Too high.")
    if guess > my_number:
    else:
    print(my_number)
if guess == my_number:
  
