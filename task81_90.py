import zlib
from timeit import Timer
import random


""""Question 81
Please write a program to randomly print a integer number between 7 and 15 inclusive.
"""


def task_81():
    return random.randrange(7, 16)


# print(task_81())


"""Question 82
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""


def task_82():
    s = 'hello world!hello world!hello world!hello world!'.encode()
    k = zlib.compress(s)
    print(k)
    print(zlib.decompress(k))


# print(task_82())


"""Question 83
Please write a program to print the running time of execution of "1+1" for 100 times.
"""


def task_83():
    t = Timer("for i in range(0,101):1+1")
    return t.timeit()


# print(task_83())


"""Question 84
Please write a program to shuffle and print the list [3,6,7,8]
"""


def task_84():
    lst = [3, 6, 7, 8]
    random.shuffle(lst)
    return lst


print(task_84())

"""Question 85
Please write a program to shuffle and print the list [3,6,7,8]
"""


def task_85():
    lst = [3, 6, 7, 8]
    random.shuffle(lst)
    return lst


print(task_85())

"""Question 86
Please write a program to generate all sentences where subject is in ["I", "You"] 
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""


def task_86():
    for i in ["I", "You"]:
        for j in ["Play", "Love"]:
            for k in ["Hockey", "Football"]:
                print(i + " " + j + " " + k)


# task_86()


"""Question 87
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
"""


def task_87():
    lst = [5, 6, 77, 45, 22, 12, 24]
    for i in lst:
        if i % 2 == 0:
            lst.remove(i)
    return lst


# print(task_87())


"""Question 88
By using list comprehension, please write a program to print the list after
 removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""


def task_88():
    lst = [12, 24, 35, 70, 88, 120, 155]
    for i in lst:
        if i % 5 == 0 and i % 7 == 0:
            lst.remove(i)
    return lst


# print(task_88())


"""Question 89
By using list comprehension, please write a program to print the list after removing the 0th,
 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""


def task_89():
    lst = [12, 24, 35, 70, 88, 120, 155]
    return [lst[i] for i in range(len(lst)) if i not in [0, 2, 4, 6]]


# print(task_89())


"""Question 90
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
"""


def task_90():
    return [[[0 for col in range(8)] for col in range(5)] for row in range(3)]


print(task_90())