# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print('Welcome to this simple calculator.')

num1 = int(input('First number: '))
num2 = int(input('Second number: '))
operation = int(input('What would you like to do with them?\n'
                  '1: Add  2: Subtract  3: Multiply  4: Divide\n'))

if operation == 1:          # addition
    answer = num1 + num2
elif operation == 2:        # subtraction
    answer = num1 - num2
elif operation == 3:        # multiplication
    answer = num1 * num2
elif operation == 4:        # division
    answer = num1 / num2

print(f'\nThe answer is {answer}\n')