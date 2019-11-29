import math
"""1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""



def one():
    lst = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 == 0:
            lst.append(str(i))
    return ','.join(lst)


# print(one())


"""2. Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def two(num):
    return 1 if num == 0 else num * two(num - 1)


# num = int(input())
# print(two(num))


"""3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def three(i):
    return {i: i * i for i in range(1, 9)}


# i = int(input())
# print(three(i))


"""4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""


def four(x):
    return x.split(','), tuple(x.split(','))


#
# x = input()
# print(four(x))


"""5. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class Five:
    def __init__(self):
        self.string = ""

    def input(self):
        self.string = input()

    def to_upper(self):
        print(self.string.upper())


# five = Five()
# five.input()
# five.to_upper()


"""6. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""


def six(d):
    c, h = 50, 30
    res = []
    for i in d.split(","):
        print(int(i))
        res.append(math.sqrt((2 * c * int(i)) / h))
    return str(res)


# d = input()
# print(six(d))


""""
7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th
 row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,...Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""


# X = int(input("Enter x = "))
# Y = int(input("Enter y = "))


def seven(x, y):
    lst = [[i * j for j in range(y)] for i in range(x)]
    return lst


# print(seven(X, Y))


"""8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
 sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""


def eight(x):
    x = x.split(",")
    x.sort()
    return ",".join(x)


# print(eight("without,hello,bag,world"))


"""
9. Write a program that accepts sequence of lines as input and prints the lines after making all characters 
in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""


def nine(x):
    return x.upper()


# print(nine("Hello world Practice makes perfect"))


"""10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


def ten(x):
    x = x.split(" ")
    return " ".join(sorted(set(x)))


print(ten("hello world and practice makes perfect and hello world again"))
