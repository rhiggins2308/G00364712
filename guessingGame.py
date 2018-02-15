# Robert Higgins 12th Feb 2018
# Guessing Game
# Adapted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

from random import randint
target = randint(1, 100)
guess = 0

print("Guess a number between 1 and 100")
while guess != target:
    guess = int(input("Please enter your guess: "))
    if guess == target:
        print("Congratulations, you guessed correctly!")
        exit
    elif guess < target:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
