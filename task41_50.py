"""Question 41
Define a function which can generate and print a tuple where the value are square of numbers between
1 and 20 (both included).
"""


def task_41():
    tpl = tuple(pow(i, 2) for i in range(1, 21))
    print(tpl)


# task_41()


"""Question 42
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
 and the last half values in one line. 
"""


def task_42():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    first = t[:(len(t) // 2)]
    second = t[(len(t) // 2):]
    print(first, '\n', second)


# task_42()


"""Question 43
Write a program to generate and print another tuple whose values are even numbers in the given tuple 
(1,2,3,4,5,6,7,8,9,10). 
"""


def task_43():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    new_t = tuple(i for i in t if i % 2 == 0)
    print(new_t)


# task_43()


"""Question 44
Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No". 
"""


def task_44(x):
    if x == "yes" or x == "YES" or x == "Yes":
        print("Yes")
    else:
        print("No")


# task_44("Yes")


"""Question 45
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
"""


def task_45():
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(filter(lambda x: x % 2 == 0, seq))
    return result


# print(task_45())


"""Question 46
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""


def task_46():
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(map(lambda x: x ** 2, seq))
    return result


# print(task_46())


"""Question 47
Write a program which can map() and filter() to make a list whose elements are square of even number in 
[1,2,3,4,5,6,7,8,9,10].
"""


def task_47():
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, seq)))
    return result


# print(task_47())


"""Question 48
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""


def task_48():
    result = list(filter(lambda x: x % 2 == 0, [i for i in range(1, 21)]))
    return result


# print(task_48())


"""Question 49
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""


def task_49():
    result = list(map(lambda x: x ** 2, [i for i in range(1, 21)]))
    return result


# print(task_49())


"""Question 50
Define a class named American which has a static method called printNationality.
"""

# class American:
#     @staticmethod
#     def printNationality():
#         print("american")
