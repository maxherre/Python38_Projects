'''
from www.practicepython.org
completed on 30.10.2020

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''
__author__: 'maxisui'

a = str(input("Please enter a word: "))
b = a[::-1]
if a == b:
    print("This word is a palindrome.")     
else:
    print("This word is not a palindrome.")