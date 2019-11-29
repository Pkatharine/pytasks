"""Question 61
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
"""

# s = input()

def task_61(s):
    u = s.encode('utf-8')
    return u


# print(task_61(s))

"""Question 62
Write a special comment to indicate a Python source code file is in unicode.
"""

# -*- coding: utf-8 -*-

"""Question 63
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


# n = int(input())


def task_63(n):
    sum = 0
    for i in range(1, n + 1):
        sum += float(float(i) / (i + 1))
    return sum


# print(task_63(n))

"""Question 64
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_64(n):
    if n == 0:
        return 1
    return task_64(n - 1) + 100


# print(task_64(5))


"""Question 65
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
13
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_65(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return task_65(n - 1) + task_65(n - 2)


# print(task_65(7))
"""Question 66
The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
"""


def task_66(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return task_65(n - 1) + task_65(n - 2)


# print(task_66(7))


"""Question 67
Please write a program using list comprehension to print the Fibonacci Sequence 
in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
"""


def task_67(n):
    if n == 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        print(task_65(n - 1) + task_65(n - 2))
        return task_65(n - 1) + task_65(n - 2)


# print(task_67(7))


"""Question 68
Please write a program using generator to print the even numbers between 0 and n in comma separated
 form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
"""


def task_68(n):
    res = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            res.append(str(i))
    return ",".join(res)


# print(task_68(int(input())))


"""Question 69
Please write a program using generator to print the numbers which can be divisible 
by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
"""


def task_69(n):
    res = []
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            res.append(str(i))
    return ",".join(res)


# print(task_69(int(input())))


"""Question 70
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
"""


def task_70():
    li = [2, 4, 6, 8]
    for i in li:
        assert i % 2 == 0


# print(task_70())