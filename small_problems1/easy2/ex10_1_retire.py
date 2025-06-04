# Build a program that displays when the user will retire and how many years she has to work till retirement.

# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

from datetime import datetime

current_year = datetime.now().year
age = int(input('What is your age? '))
retirement = int(input('At what age would you like to retire? '))
years_left = retirement - age

print()
print(f"It's {current_year}. You will retire in {current_year + years_left}")
print(f"You have only {years_left} years of work to go!")