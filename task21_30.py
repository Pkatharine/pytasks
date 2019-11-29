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


def task_21(s):
    x, y = 0, 0
    while True:
        s = s.split("")
        if not s:
            break
        if s[0] == 'UP':
            x -= int(s[1])
        if s[0] == 'DOWN':
            x += int(s[1])
        if s[0] == 'LEFT':
            y -= int(s[1])
        if s[0] == 'RIGHT':
            y += int(s[1])
    return round(math.sqrt(pow(x, 2) + pow(y, 2)))


# s = input()
# print(task_21(s))


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
    x = x.split()
    st = sorted(set(x))
    for i in st:
        print("{0}:{1}".format(i, st.count(i)))


task_22("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")

"""Question 23
Write a method which can calculate square value of number
"""


def task_23(x):
    """
    :param x: main parameter that must be calculate square value
    :return: square value of x number
    """
    return x ** 2


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


"""Question 27
Define a function that can convert a integer into a string and print it in console.
"""


def task_27(x):
    return str(x)


print(task_27(9999))

"""Question 29
Define a function that can receive two integral numbers in string form
 and compute their sum and then print it in console.
"""


def task_29(x):
    x = x.split(" ")
    return int(x[0]) + int(x[1])


# print(task_29("10 20"))


"""Question 30
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""


def task_30(x, y):
    return x + y

# print(task_30("hey", "world"))
