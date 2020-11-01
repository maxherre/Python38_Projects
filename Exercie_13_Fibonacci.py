'''
from www.praticepython.com
completed on 01.11.2020

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''
__author__:'maxisui'

userinput = int(input("How many numbers from the Fibonacci sequence should be calculated? "))

def cal_fibon(count):
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count -1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

print(cal_fibon(userinput))