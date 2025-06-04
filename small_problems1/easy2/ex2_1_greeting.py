# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

user_name = input('What is your name? ')

if (user_name[-1]) == '!':
    print(f'HELLO {user_name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {user_name}.')