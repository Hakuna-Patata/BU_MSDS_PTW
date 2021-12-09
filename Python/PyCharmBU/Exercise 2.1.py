# Program: Fiber Optic Cable Cost Calculator
# Purpose: This program calculates the parts cost to install Fiber Optic cabling
# Developer: Patrick Weatherford
# Week 2 - Assignment 2.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

cost_per_foot = 0.87  # variable for the cost per foot
print('Hello there Fiber Optic cable aficionado!')
input('Press Enter to continue...')  # welcome message
org = input("Enter your business organization:")  # business name
cable_feet = float(input("Enter the length (in feet) of cable needed:"))  # variable to get length needed
total = 1.00 * cable_feet * cost_per_foot  # the total cost
print('\r')
print('Invoice for', org)
print('Feet of cable needed: ', cable_feet, 'ft.', sep='')
print('Cost per foot : $', cost_per_foot, sep='')
print('Total: $', "{:.2f}".format(total), sep='')


