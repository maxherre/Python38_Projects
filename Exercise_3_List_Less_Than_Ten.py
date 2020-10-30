'''
from www.practicepython.org
completed on 29.10.2020

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 8.
'''
__author__ = 'maxisui'
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for element in a:
    if element < 8:
        print(element)
'''
Extras:
Instead of printing the elements one by one, make a new list that has all the elements less than 8 from this list in it. 
Print out this new list. Write this in one line of Python.
'''
for element in a:
    if element < 8:
        b.append(element)
print(b)
'''
Ask the user for a number and return a list that contains only elements from the original list 'a' that are smaller than that number given by the user.
'''
c = int(input("Choose a number between 0 and 100: "))
for element in a:
    if element < c:
        b.append(element)
print(b)

