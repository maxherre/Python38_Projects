'''
from www.practicepython.org
completed on 29.10.2020
Create a programm that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year
that they will turn 100 years old. 
Extras:
- Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
- Print out as many copies of the previous message on separate lines.
'''
__author__ = 'maxisui'
name = input("Give me your name: ")
age = int(input("What is your age? "))
years = str((100 - age) + 2020)
print( name + " will turn 100 in the year " + years)