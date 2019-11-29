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


# print(task_31("hey", "world"))


"""Question 32
Define a function that can accept an integer number as input and print the "It is an even number" 
if the number is even, otherwise print "It is an odd number".
"""


def task_32(x):
    return "It is an even number" if x % 2 == 0 else "It is an odd number"


# print(task_32(6))


"""Question 33
Define a function which can print a dictionary where the keys are numbers between 1 and 3 
(both included) and the values are square of keys.
"""


def task_33():
    d = dict()
    for i in range(1, 4):
        d[i] = pow(i, 2)
    print(d)


# task_33()


"""
Question 34
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
 and the values are square of keys.
"""


def task_34():
    d = dict()
    for i in range(1, 21):
        d[i] = pow(i, 2)
    print(d)


# task_34()


"""Question 35
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
 and the values are square of keys. The function should just print the values only.
"""


def task_35():
    d = dict()
    for i in range(1, 21):
        d[i] = pow(i, 2)
    print(d.values())


# task_35()


"""Question 36
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys. The function should just print the keys only.
"""


def task_36():
    d = dict()
    for i in range(1, 21):
        d[i] = pow(i, 2)
    return d.keys()


# print(task_36())


"""Question 37
Define a function which can generate and print a list where the values are square of numbers
 between 1 and 20 (both included).
"""


def task_37():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res)


# task_37()


"""Question 38
Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the first 5 elements in the list.
"""


def task_38():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res[:5])


# task_38()


"""Question 39
Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the last 5 elements in the list.
"""


def task_39():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res[-5:])


# task_39()


"""Question 40
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
 Then the function needs to print all values except the first 5 elements in the list.
"""


def task_40():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res[5:])


# task_40()

