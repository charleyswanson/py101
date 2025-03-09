def prompt(message):
    print(f'==> {message}')

def invalid_number(input_number):
    try:
        int(input_number)
    except ValueError:
        return True

    return False

prompt('Welcome to this simple calculator.')

prompt('First number:')
num1 = input()

while invalid_number(num1):
    prompt("That's not a valid number, please try again.")
    num1 = input()

prompt('Second number:')
num2 = input()

while invalid_number(num2):
    prompt("That's not a valid number, please try again.")
    num2 = input()

prompt(('What would you like to do with them?\n'
       '1: Add  2: Subtract  3: Multiply  4: Divide'))
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('Please enter 1, 2, 3 or 4:')
    operation = input()

match operation:
    case '1':                           # addition
        answer = int(num1) + int(num2)
    case '2':                           # subtraction
        answer = int(num1) - int(num2)
    case '3':                           # multiplication
        answer = int(num1) * int(num2)
    case '4':                           # division
        answer = int(num1) / int(num2)

prompt(f'The answer is {answer}')