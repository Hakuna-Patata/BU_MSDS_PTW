# Program: Fiber Optic Cable Cost Calculator
# Purpose: This program calculates the parts cost to install Fiber Optic cabling
# Developer: Patrick Weatherford
# Week 2 - Assignment 2.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

nl = '\n'

print('Hello there Fiber Optic cable aficionado!')
input('Press Enter to continue...')  # welcome message
org = input("Enter your business organization:")  # business name
cable_feet = float(input("Enter the length (in feet) of cable needed:"))  # variable to get length needed

if 100 < cable_feet <= 250:
    cost_per_foot = 0.8
elif 250 < cable_feet <= 500:
    cost_per_foot = 0.7
elif cable_feet > 500:
    cost_per_foot = 0.5
else:
    cost_per_foot = 0.87

total = 1.00 * cable_feet * cost_per_foot  # the total cost

print(f"{nl}Invoice for {org}{nl}Cost per foot: ${cost_per_foot}{nl}Total: ${total:.2f}")
