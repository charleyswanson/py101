# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

# Teddy is 69 years old!

# You may find the randint function from the random module useful.

# Modify this program to ask for a name, then print the age for that person. For an extra challenge, use "Teddy" as the name if no name is entered.

from random import randint

user_name = input("What's your name? ")

if not user_name: 
    user_name = "Teddy"

print(f"{user_name} is {randint(20, 100)} years old!")