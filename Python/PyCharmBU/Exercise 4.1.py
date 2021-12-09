# Program: Fiber Optic Cable Cost Calculator
# Purpose: This program calculates the parts cost to install Fiber Optic cabling
# Developer: Patrick Weatherford
# Week 2 - Assignment 4.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

nl = '\n'  # Used for new line in f'string

print(f"Hello there fiber optic cable aficionado!{nl}")  # Welcome message
print(f"{input('Press Enter to continue...')}")
org = input('Enter your business organization:')  # business name
cable_feet = float(input('Enter the length (in feet) of cable needed:'))  # user input variable for feet required
og_price = 0.87  # Starting price


def cost_calculator(feet, price):  # define function and default price to 0.87 per foot
    feet = cable_feet
    price = og_price
    # Calculate discount based on feet needed
    if 100 < feet <= 250:
        price = 0.8
    elif 250 < feet <= 500:
        price = 0.7
    elif feet > 500:
        price = 0.5
    else:
        price = 0.87

    # Calculate total
    total = 1.00 * feet * price
    print(f"{nl}Invoice for {org}{nl}Cost per foot: ${price}{nl}Total: ${total:.2f}")  # Print invoice with cost


cost_calculator(feet, price)
