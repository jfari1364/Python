"""
This is a 'Guess the Number' program that requires a user to guess a
number between 1 and 20. The user then has 6 guesses
until the program quits and tells the user what that number was.
"""

import random

name = input("Hello, what is your name? ").title()
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

# Assigns the variable 'secretNumber' a random number value
secretNumber = random.randint(1, 20)

def guess_number():
    # Allows a user to have 6 guesses and inform the user if their guess
    # is either too low or too high
    for guessesTaken in range(1, 7):
        guess = int(input("\nTake a guess: "))
        
        if guess < secretNumber:
            print("Your guess is too low.")
            
        elif guess > secretNumber:
            print("Your guess is too high.")
            
        else:
            break

    # Two statements that will be printed if the user is able to guess the number,
    # or if the user is unable to guess the number.
    if guess == secretNumber:
        print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")

    else:
        print("Nope. The number I was thinking of was " + str(secretNumber))


if __name__ == "__main__":
    guess_number()

    
