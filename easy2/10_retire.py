# Build a program that displays when the user will retire and how many years she has to work till retirement.

# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

from datetime import datetime

year_now = datetime.now().year

current_age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
work_years_left = retirement_age - current_age

print(f"It's {year_now}. You will retire in {year_now + work_years_left}.\n"
      f"You only have {work_years_left} years of work to go!"
)