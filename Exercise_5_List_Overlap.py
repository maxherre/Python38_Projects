'''
from www.practicepython.org
completed on 30.10.2020

Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
'''
__author__ = 'maxisui'


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for elements in a and b:
    if elements in a and b:
        c.append(elements)
print(c)

'''
Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''
import numpy as np

d = list(np.random.randint(1,100,25))
e = list(np.random.randint(1,100,45))
f = []

for elem in d and e:
    if elem in d and e:
        f.append(elem)
print(f)

