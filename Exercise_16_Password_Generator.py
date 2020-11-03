''' from www.praticepython.org
completed on 03.11.2020

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
__author__: 'maxisui'

import random

def pwgen():
    length = int(input("How many characters should your password have? "))
    letters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    pw = "".join(random.sample(letters, length ))
    print(pw)
pwgen()