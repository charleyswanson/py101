import json

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'MESSAGES' contains the loaded messages as a Python dictionary

def prompt(message):
    print(f'==> {message}')

def invalid_number(input_number):
    try:
        int(input_number)
    except ValueError:
        return True

    return False

prompt(MESSAGES['welcome'])
keep_going = 'y'

while True:
    prompt(MESSAGES['num1'])
    num1 = input()

    while invalid_number(num1):
        prompt(MESSAGES['invalid_num'])
        num1 = input()

    prompt(MESSAGES['num2'])
    num2 = input()

    while invalid_number(num2):
        prompt(MESSAGES['invalid_num'])
        num2 = input()

    prompt(MESSAGES['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES['invalid_operation'])
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
    prompt('Would you like to run more numbers? (y to continue)')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break
    print()