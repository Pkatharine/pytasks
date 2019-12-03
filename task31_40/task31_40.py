"""Question 31
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.
"""


def task_31(x, y):
    if len(x) > len(y):
        return x
    elif len(x) < len(y):
        return y
    else:
        return x + '\n' + y

#print(task_31("hey", "world"))


"""Question 32
Define a function that can accept an integer number as input and print the "It is an even number" 
if the number is even, otherwise print "It is an odd number".
"""


def task_32(x):
    return "It is an even number" if x % 2 == 0 else "It is an odd number"


#print(task_32(-6))


"""Question 33
Define a function which can print a dictionary where the keys are numbers between 1 and 3 
(both included) and the values are square of keys.
"""


def task_33(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = pow(i, 2)
    return d


#print(task_33(int(input())))


"""
Question 34
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
 and the values are square of keys.
"""


def task_34(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = pow(i, 2)
    return d


#print(task_34(int(input())))


"""Question 35
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
 and the values are square of keys. The function should just print the values only.
"""


def task_35(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = pow(i, 2)
    return str(d.values())


#print(task_35(int(input())))


"""Question 36
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys. The function should just print the keys only.
"""


def task_36(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = pow(i, 2)
    return str(d.keys())


#print(task_36(int(input())))


"""Question 37
Define a function which can generate and print a list where the values are square of numbers
 between 1 and 20 (both included).
"""


def task_37(n):
    res = []
    for i in range(1, n+1):
        res.append(pow(i, 2))
    return res


#print(task_37(int(input())))


"""Question 38
Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the first 5 elements in the list.
"""


def task_38(n):
    res = []
    for i in range(1, n+1):
        res.append(pow(i, 2))
    return (res[:5])


#print(task_38(int(input())))


"""Question 39
Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the last 5 elements in the list.
"""


def task_39(n):
    res = []
    for i in range(1, n+1):
        res.append(pow(i, 2))
    return (res[-5:])


#print(task_39(int(input())))


"""Question 40
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
 Then the function needs to print all values except the first 5 elements in the list.
"""


def task_40(n):
    res = []
    for i in range(1, n+1):
        res.append(pow(i, 2))
    return (res[5:])


#print(task_40(int(input())))

