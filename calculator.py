"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

quit = False

while quit is False:
    read_expression = raw_input()

    if read_expression != 'q':

        read_expression = read_expression.split(' ')
        operator = read_expression[0]

        num_args = len(read_expression)
        num = []
        print num_args
        print read_expression

        for i in range(1, num_args):

            print i
            num[i-1] = int(read_expression[i])

        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
            'square': square,
            'cube': cube,
            'power': power,
            'mod': mod
        }

        if operator in operations and num_args == 3:
            print operations[operator](num[1], num[2])
        elif operator in operations and num_args == 2:
            print operations[operator](num[1])

    else:
        quit = True
