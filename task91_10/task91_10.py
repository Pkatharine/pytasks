import itertools


"""Question 91
By using list comprehension, please write a program to print the list after
 removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""


def task_91():
    lst = [12, 24, 35, 70, 88, 120, 155]
    return [lst[i] for i in range(len(lst)) if i not in [0, 4, 5]]


# print(task_91())


"""Question 92
By using list comprehension, please write a program to print the list after removing the 
value 24 in [12,24,35,24,88,120,155].
"""


def task_92():
    lst = [12, 24, 35, 24, 88, 120, 155]
    return list(filter(lambda a: a != 24, lst))


#print(task_92())


"""
Question 93
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the above given lists.
"""


def task_93():
    lst = [1, 3, 6, 78, 35, 55]
    lst1 = [12, 24, 35, 24, 88, 120, 155]
    res = []
    for i in lst:
        for j in lst1:
            if i == j:
                res.append(i)
    return res


#print(task_93())


"""Question 94
With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.
"""


def task_94():
    lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res


#print(task_94())


"""
Question 95
Define a class Person and its two child classes: Male and Female.
 All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""


class Person:
    def getGender(self):
        return ("Person")


class Male(Person):
    def getGender(self):
        return ("Male")


class Female(Person):
    def getGender(self):
        return ("Female")

person = Person()
male = Male()
female = Female()
#print(person.getGender())
#print(male.getGender())
#print(female.getGender())


"""Question 96
Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""


def task_96(string):
    st = set(string)
    dict = {i: string.count(i) for i in st}
    dict = {key: dict[key] for key in sorted(dict.keys())}
    for i in dict.keys():
        print(str(i) + "," + str(dict[i]))


#task_96(input())

"""Question 97
Please write a program which accepts a string from console and print it in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
"""


def task_97(x):
    return x[::-1]


# print(task_97(input()))


"""Question 98
Please write a program which accepts a string from console and print the characters that have even indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
"""


def task_98(x):
    return x[::2]


# print(task_98(input()))


"""Question 99
Please write a program which prints all permutations of [1,2,3]
"""


def task_99():
    return list(itertools.permutations([1, 2, 3]))


#print(task_99())


"""Question 100
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
 How many rabbits and how many chickens do we have?
"""


def task_100(head, leg):
    rabbits = leg // 2 - head
    chickens = head - rabbits
    return (rabbits, chickens)

#print(task_100(35, 94))
