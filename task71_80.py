import math
import random
"""Question 71
Please write a program which accepts basic mathematic expression from console and print the evaluation result.
Example:
If the following string is given as input to the program:
35+3
Then, the output of the program should be:
38
"""


def task_71(expression):
    return eval(expression)


# print(task_71(input()))

"""Question 72
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.
"""


def task_72(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


# print(task_72([2, 5, 7, 9, 11, 17, 222], 5))


"""Question 73
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.
"""


def task_73(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


# print(task_73([2, 5, 7, 9, 11, 17, 222], 5))


"""Question 74
Please generate a random float where the value is between 10 and 100 using Python math module.
"""


def task_74():
    return random.uniform(10.0, 100.0)


# print(task_74())


"""Question 75
Please generate a random float where the value is between 5 and 95 using Python math module.
"""


def task_75():
    return random.uniform(5.0, 95.0)


# print(task_75())


"""
Question 76
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
"""


def task_76():
    return [random.randrange(0, 10, 2)]


# print(task_76())


"""Question 77
Please write a program to output a random number, which is divisible by 5 and 7,
 between 0 and 10 inclusive using random module and list comprehension.
"""


def task_77():
    return random.choice([i for i in range(0, 11) if i % 5 == 0 and i % 7 == 0])


# print(task_77())

"""Question 78
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
"""


def task_78():
    return random.sample(range(100, 201), 5)


# print(task_78())


"""Question 79
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
"""


def task_79():
    return random.sample([i for i in range(100, 201) if i % 2 == 0], 5)


# print(task_79())


"""Question 80
Please write a program to randomly generate a list with 5 numbers, 
which are divisible by 5 and 7 , between 1 and 1000 inclusive.
"""


def task_80():
    return random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5)


# print(task_80())
