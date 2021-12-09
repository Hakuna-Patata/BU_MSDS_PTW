# Program: Input Calculation and Average
# Purpose: This program will perform various calculations on values input by the user
# Developer: Patrick Weatherford
# Week 2 - Assignment 5.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

nl = '\n'  # Used for line break in f-string function
operator_list = ['+','-','*','/']  # create list with valid operators to select from
operator = input(f"{nl}***********************{nl}2 Parameter Calculator{nl}***********************{nl}Enter operator to use(+,-,*,/):")
while True:  # loop until user enters a valid operator to use
    if operator in operator_list:
        break
    else:
        operator = input('Invalid operator! Please enter an operator to use(+,-,*,/):')


def performCalculation(operator):
    for i in range(1,3):  # Only need to values for the calculation.
        if i == 1:
            val1 = input('Enter 1st number:')  # If first loop, get value and assign to val1 variable
            while True:  # loop until user enters a valid number for val1
                if val1.isnumeric():
                    break
                val1 = input('Invalid number! Enter 1st number:')
        else:
            val2 = input('Enter 2nd number:')  # If second loop, get value and assign to val2 variable
            while True:  # loop until user enters a valid number for val2
                if val2.isnumeric():
                    break
                val2 = input('Invalid number! Enter 2nd number:')
        i += 1
    val1 = float(val1)  # convert val1 input to float
    val2 = float(val2)  # convert val2 input to float
    # Calculation ov val1 & val2 below
    if operator == '+':
        calc = val1 + val2
    elif operator == '-':
        calc = val1 - val2
    elif operator == '*':
        calc = val1 * val2
    else:
        calc = val1 / val2
    print(f"...{nl}{val1} {operator} {val2} = {calc}{nl}")  # print result


def calculateAverage():
    print(f"{nl}*******************{nl}Average Calculator{nl}*******************")
    sum_of_numbers = 0  # start of sum is 0
    while True:
        n = input(f"How many numbers will be used?")
        try:
            n = int(n)
            if n > 0:
                break
            else:
                print("Numbers being used must be greater than zero, try again!")
        except:
            print("Entry was not a number, try again!")
    for i in range(0,n):
        val = input(f"Enter value {str(i+1)}:")
        while not val.isnumeric():
            val = input(f"Value not a number, try again! Enter value {str(i+1)}:")
        sum_of_numbers += float(val)

    print(f"...{nl}Total: {sum_of_numbers}{nl}Average: {sum_of_numbers / n}")


performCalculation(operator)
calculateAverage()
