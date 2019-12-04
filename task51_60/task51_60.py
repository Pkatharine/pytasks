import math


"""Question 51
Define a class named American and its subclass NewYorker. 
"""


class American():
    def __init__(self):
        pass


class NewYorker(American):
    def __init__(self):
        super().__init__()


"""Question 52
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


#circle = Circle(5)
#print(circle.area())


"""Question 53
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area. 
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length + self.width) * 2


# rect = Rectangle(5, 4)
# print(rect.area())


"""Question 54
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


# sq = Square(3)
# print(Square().area())
# print(sq.area())


"""Question 55
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""


def task_55(n):
    try:
        return n / 0
    except ZeroDivisionError:
        return "You are dividing a number by ZERO!"


#print(task_55(int(input())))


"""Question 56
Define a custom exception class which takes a string message as attribute.
"""


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


"""Question 57
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_57(x):
    return x[:x.find('@')]


# x = input()
#print(task_57(input()))


"""Question 58
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print 
the company name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_58(x):
    return x[x.find('@') + 1:x.find('.com')]


# x = input()
#print(task_58(input()))


"""Question 59
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed 
of digits only.Example:
If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_59(x):
    x = x.split()
    return [i for i in x if i.isdigit()]


#print(task_59(input()))


"""Question 60
Print a unicode string "hello world".
"""


def task_60():
    return u"hello world"

#print(task_60())
