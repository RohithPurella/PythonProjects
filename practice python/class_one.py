import os
from os import path
from numpy import arange
import numpy

print("Hello world")
number = input("enter ur fav number here: ")

enter = input("enter any thing here: ")
directory = "output/output.txt"
myFile = open(directory, "r")
myFile.write(enter,)

myFile.close()
print(myFile)




# if statements

x = float(input("input integer : "))
if x == 0:

    print("zero")

elif x < 0:
    print("negative number")
elif x > 0:
    print("possitive number")
else:
    print("more")

# for statement:
# Measure some strings:

words = ["car", "cab", "defination", "windows"]

for w in words:
    print(w, len(w))

for i in range(100):
    print(i)

count = 0
while count == 0:
    print('The count is:')
    count = count + 1

print("Good bye!")

i == True

while i:
    if i < 10000:
        print(i)
        i += 1
    else:
        break

print("bye")

a = ["marry", "james", "pranay", "rohith"]
for i in range(len(a)):
    print(i, a[i])

v = list(range(4))
print(v)

for num in range(2, 10):
    if num % 2 == 0:
        print("found an even number ", num)
        continue
    print("Found a numbwer", num)

# pass statements:

while True:
    print("hello while pass")
    pass  # Busy-wait for kwyboard interrupt (ctrl + c)
    break  # used for break the loop


# Class
class MyEmptyClass:
    print("hello class")
    pass


# def functions
def initlog(*args):
    print(*args)
    pass  # remember to implement this


# Defining Functions
# We can create a function that writes the Fibonacci series to an arbitrary boundary:

# >>>
# >>> def fib(n):
# ...     """Print a Fibonacci series up to n."""
# ...     a, b = 0, 1
# ...     while a < n:
# ...         print(a, end=' ')
# ...         a, b = b, a+b
# ...     print()
# ...
# >>> # Now call the function we just defined:
# ... fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

def fib(n):  # write Fibonacci series up to n

    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(3000)

f = fib
print(f(100))


# 4.7. More on Defining Functions
# It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

# 4.7.1. Default Argument Values


def ask_ok(prompt, retries=4, reminder="please try again!"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
    if ok in ("n", "no", "nop", "nope"):
        return False
        retries = retries - 1
    if retries < 0:
        raise ValueError("invalid user response")
        print(reminder)


i = 5


def f(arg=i):
    print(arg)


i = 6
f()

f("kill me")
"""

output for below statement
""[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]

"""


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
print(f(4))


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot("1000")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("lamburgani")



def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        return  "FizzBuzz"
    if input % 3 == 0 :
        return "Fuzz"
    if input % 5 == 0 :
        return "Buzz"
    return input

print(fizz_buzz(int(input("> Enter a number: "))))