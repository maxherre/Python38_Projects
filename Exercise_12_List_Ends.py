'''
from www.practicepython.org
completed on 01.11.2020

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''
__author__: 'maxisui'

a = [5, 10, 15, 20, 25, 30]
b = []

def list_maker(lista):
    b.append(lista[0])
    b.append(lista[-1])

list_maker(a)
print(b)