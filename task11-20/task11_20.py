import re

"""11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""


def task_11(x):
    res = []
    for i in x.split(","):
        if int(i, 2) % 5 == 0:
            res.append(i)
    return ",".join(res)


# print(task_11("0100,0011,1010,1001"))


"""
Question 12
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each 
digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def task_12():
    res = []
    for i in range(1000, 3001):
        i = str(i)
        if (int(i[0]) % 2 == 0) and (int(i[1]) % 2 == 0) and (int(i[2]) % 2 == 0) and (int(i[3]) % 2 == 0):
            res.append(i)

    return ",".join(res)

#print(task_12())


"""Question 13
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""


def task_13(x):
    num, let = 0, 0
    for i in x:
        if i.isalpha():
            let = let + 1
        elif i.isdigit():
            num = num + 1
    return "LETTERS " + str(let) + '\n' + "DIGITS " + str(num)


#print(task_13("hello world! 123"))


"""Question 14
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


def task_14(x):
    upp, low = 0, 0
    for i in x:
        if i.islower():
            low = low + 1
        elif i.isupper():
            upp = upp + 1
    return "UPPER CASE " + str(upp) + '\n' + "LOWER CASE " + str(low)


# print(task_14("Hello world!"))


"""Question 15
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""


def task_15(x):
    x = str(x)
    return int(x) + int(x * 2) + int(x * 3) + int(x * 4)


#print(task_15(9))


"""Question 16
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
"""


def task_16(x):
    res = []
    x = x.split(",")
    for i in x:
        if int(i) % 2 == 1:
            res.append(int(i) * int(i))
    return str(res)[1:-1]


#print(task_16('1,2,3,4,5,6,7,8,9'))


"""Question 17
Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

# def task_17(x):


"""Question 18
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""


def task_18(x):
    res = []
    x = x.split(",")
    for i in x:
        if 6 > len(i) > 12:
            continue
        else:
            pass
        if not re.search("[a-z]", i):
            continue
        elif not re.search("[0-9]", i):
            continue
        elif not re.search("[A-Z]", i):
            continue
        elif not re.search("[$#@]", i):
            continue
        elif re.search('\s', i):
            continue
        else:
            pass
        res.append(i)
    return ",".join(res)


#print(task_18("ABd1234@1,a F1#,2w3E*,2We3345"))


"""Question 19
You are required to write a program to sort the (name, age, height) tuples 
by ascending order where name is string, age and height are numbers. The tuples are input by console. 
The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""


def task_19(x):
    lst = []
    while True:
        x = input().split(',')
        if not x[0]:
            break
        lst.append(tuple(x))
    lst.sort(key=lambda x: (x[0], x[1], x[2]))
    return lst


# print(task_19(input()))


"""Question 20
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""


class Iterator(object):
    def __init__(self, n):
        super(Iterator, self).__init__()
        self.n = n

    def div_by_seven(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i

# for num in Iterator(100).div_by_seven():
#     print(num)
