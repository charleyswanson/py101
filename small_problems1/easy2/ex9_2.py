# Further Exploration
# Modify this program to ask for a name, then print the age for that person. For an extra challenge, use "Teddy" as the name if no name is entered.

import random

age = random.randint(20, 100)
name = input('What is your name? ')

# name = input('What is your name? ') or 'Teddy' 

if name == '':
    name = 'Teddy'

print(f'{name} is {age} years old!')