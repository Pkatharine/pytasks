import math

"""Question 21
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, 
DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current 
position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""


def task_21(x):
    s = x.split(" ")
    x, y = 0, 0
    for i in range(0, len(s) - 1):
        if s[i] == 'RIGHT':
            x = x + int(s[i + 1])
        elif s[i] == 'LEFT':
            x = x - int(s[i + 1])
        elif s[i] == "UP":
            y = y + int(s[i + 1])
        elif s[i] == "DOWN":
            y = y - int(s[i + 1])
    return int(math.sqrt(x ** 2 + y ** 2))


#print(task_21(input()))


"""Question 22
Write a program to compute the frequency of the words from the input. The output should output after sorting
 the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""


def task_22(x):
    sort = x.split()
    dict = {i: sort.count(i) for i in sort}
    dict = sorted(dict.items())
    return dict


#print(task_22(input()))


"""Question 23
Write a method which can calculate square value of number
"""


def task_23(x):
    """
    :param x: main parameter that must be calculate square value
    :return: square value of x number
    """
    return x ** 2
#print(task_23(int(input())))


"""Question 24
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. 
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
"""

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# print(task_23.__doc__)


"""Question 25
Define a class, which have a class parameter and have a same instance parameter.
"""


class Task25:
    x = "Person"

    def __init__(self, x=None):
        self.x = x


"""Question 26
Define a function which can compute the sum of two numbers.
"""


def task_26(x, y):
    return x + y

#print(task_26(int(input())))

"""Question 27
Define a function that can convert a integer into a string and print it in console.
"""


def task_27(x):
    return str(x)


#print(task_27(999))

"""Question 29
Define a function that can receive two integral numbers in string form
 and compute their sum and then print it in console.
"""


def task_29(x):
    x = x.split(" ")
    return int(x[0]) + int(x[1])


#print(task_29("10 20"))


"""Question 30
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""


def task_30(x, y):
    return x + y

print(task_30("", ""))
