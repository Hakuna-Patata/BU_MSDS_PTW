# Program: Temperature Journal
# Purpose: This program gets temperature inputs from the user and stores them in a list. Certain values are then retrieved.
# Developer: Patrick Weatherford
# Week 2 - Assignment 6.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller


nl = '\n'
temperatures = []
print(f"********************{nl}Temperature Journal{nl}********************")
user_input = input(f"Enter temperature to record (enter 'exit' when complete):")

while user_input.upper() != 'EXIT':
    try:
        user_input = float(user_input)
        temperatures.append(user_input)
        user_input = input(f"Enter another temperature (or enter 'exit' when completed)")
    except:
        user_input = input(f"Not a number, try again!")

print(f"""...{nl}...
Temperatures recorded: {temperatures}
Largest temp recorded: {max(temperatures)}
Smallest temp recorded: {min(temperatures)}
Total temps recorded: {len(temperatures)}
""")
