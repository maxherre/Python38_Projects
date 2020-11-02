''''
from www.practicepyton.com
completed on 01.11.2020

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
__author__: 'maxisui'

import random

a = [random.randint(0,30) for i in range(10)]

def duplicator(list):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b 

print(a)
print(duplicator(a))