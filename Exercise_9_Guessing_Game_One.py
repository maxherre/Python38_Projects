'''
from www.practicepython.org
completed on 30.10.2020

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
__author__: 'maxisui'

import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("Choose a number between 1 and 9: ")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print("You guessed too low!")
    elif guess > number:
        print("You guessed to high!")
    else:
        print("You got it!!!")
        print("And it only took you",count,"tries!")