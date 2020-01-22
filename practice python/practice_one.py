import os
from os import path

from _collections import deque

# Types of outputs:
print("Hello rohit purella")
print('single colons')
print("Double colons")
print("""Triple colons for multi line comments and paragraphs like this:
 qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm
 qwertuiopasdfghjklzxcvbnm
 qazxcvbnmnlopikjuhygtfresw
 """)
print(f"you can type anything and ani symbol's in it but no double colons")
print("rohith\"s")
print(r'c:users\name we use "r" to avoid "\n"which is used for break the, "print" or output to next line')

# input by user
print(input("> enter fav color here: "))

# Data Types:

a = int("9")
print(a)

a = input("> enter a your fav movie name here: ")
b = a
print("fav movie is {}".format(b))

# Lists:
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)
print(number[2:7])

# Fibonacci series calculate by adding two two variables in list:
a, b = 2, 3

while a < 60:
    print(a)
    a, b = a, a + b
    break

# If Statements:
x = int(input("enter x = "))

if x < 0:
    x = 0
    print("not a negative number")
elif x == 0:
    print('Negative changed to zero')

elif x == 1:
    print('Single')
else:
    print('More')
########################################## problem in coding ############################################
print(""" INSTRUCTIONS FOR GAME
type input as start to start the code game
type input as stop to stop the code game
type input as exit to exit the code game""")

insert = "stop"

while True:
    insert = input("inter a commands here: ")

    if insert == "start":
        print("your game started...")

    elif insert == "stop":
        print("your game is stoped...")

    elif insert == "exit":
        print("your going to exit ......")
        break

# For statement:
words = str([1, 2, 4, 3, 5, 6, 7, 8])
for w in words:
    print(w, len(w))

for i in range(100):
    i = i / 2
    print(i)

names = ["rohit", "sai", "roshitha", "roshini", "suraj"]
for name in range(len(names)):
    print(name, names[name])
    print(list(names))

# Pass Statements

while True:
    print("pass passed in while loop")
    break  # added break to stop loop
    pass


def initlog(*args):
    print("pass is passed  in def {}".format(*args))
    pass


initlog("is it?")


class MyEmptyClass:
    print("from my empty class")
    pass


# fib
def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

    #### Now call the function we just defined######


fib(2000)


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
print(f(4))


# Keyword argments and tuples
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(input(">enter your fav car here: "))

# Lambda Expressions it is an anonymous function:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)

squares = list(map(lambda x: x ** 2, range(10)))


# Intermezzo: Coding Style:


# Arbitrary Argument Lists:
# def write_multiple_items(file, separator, *args):
#  file.write(separator.join(args))


def concat(*args, sep="/"):
    return sep.join(args)


concat("earth", "mars", "venus")
'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'

# Data structures :
# 5.1. More on Lists
#
#
#
#
#

#
#
#
#
#

"""
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:]."""

# EXAMPLE for List data structures
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana')
fruits.count('tangerine')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits
fruits.append('grape')
fruits
fruits.sort()
fruits
fruits.pop()

# USING QUEUES IN LISTS

queue = deque(["eric", "Rama", "Rohit"])
queue.append("srinivas")
queue.popleft()
queue.append("saisri")
print(queue)

# USING ZIP
matrix_example = [
    [1, 2, 3, 4],
    [7, 8, 5, 9],
    [5, 6, 85, 4],
]

list(zip(matrix_example))
# del statement
del matrix_example[0]
print(matrix_example)

# Tuples and Sequences:

t = 3469, 94326, "rohit"
print([0])
print(t)

# Sets
basket = {'apple', 'orange', 'apple', 'orange', 'banana'}
print(basket)
'orange' in basket
'crabgrass' in basket
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
# Looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for l, m in knights.items():
    print(l, m)


