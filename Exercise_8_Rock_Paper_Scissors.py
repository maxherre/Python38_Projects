'''
from www.practicepython.org
completed on 30.10.2020

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''
__author__: 'maxisui'
import sys
player1 = input("Player 1: What is your name?")
player2 = input("Player 2: What is your name?")

player1_answer = input("%s, choose your weapon: 'Rock', 'Paper' or 'Scissors'" % player1)
player2_answer = input("%s, choose your weapon: 'Rock', 'Paper' or 'Scissors'" % player2)

def RockPaperScissor(p1, p2):
    if p1 == p2:
        return("It's a tie!!!")
    elif p1 == 'Rock':
        if p2 == 'Scissors':
            return("Rock beats Scissors. %s wins!!!" % player1)
        else:
            return("Paper beats Rock. %s wins!!!" % player2)
    elif p1 == 'Scissors':
        if p2 == 'Paper':
            return("Scissors beat Paper. %s wins!!!" % player1)
        else:
            return("Rock beats Scissors. %s wins!!!" % player2)
    elif p1 == 'Paper':
        if p2 == 'Rock':
            return("Paper beats Rock. %s wins!!!" % player1)
        else:
            return("Scissors beat Paper. %s wins!!!" % player2)
    else:
        return("Invalid input! You have not entered Rock, Paper or Scissors. Try again :)")
        sys.exit()
print(RockPaperScissor(player1_answer, player2_answer))
