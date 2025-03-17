import json
import os
import platform

# Load the messages from the JSON file
with open('calculator_loan_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def prompt(message):
    print(f'>-- {message}')
    print('    ', end='')

def prompt_error(message):
    print(f'    {message}')
    print('    ', end='')

def prompt_dollar(message):
    print(f'>-- {message}')
    print('    $', end='')

def prompt_error_dollar(message):
    print(f'    {message}')
    print('    $', end='')

def invalid_int(number):
    try:
        int(number)
    except ValueError:
        return True
    if int(number) <= 0:
        return True

    return False

def invalid_float(number):
    try:
        float(number)
    except ValueError:
        return True
    if float(number) < 0:
        return True

    return False

def get_loan_amount():
    # get loan amount, verify input, return an integer
    prompt_dollar(MESSAGES['msg_loan_amount'])
    loan_amount = input()

    while invalid_int(loan_amount):
        prompt_error_dollar(MESSAGES['msg_invalid_int'])
        loan_amount = input()

    return int(loan_amount)

def get_apr():
    # get APR, verify input, convert to montly APR, return a float
    print()
    prompt(MESSAGES['msg_apr'])
    apr = input()

    if apr == 0:
        return apr

    while invalid_float(apr):
        prompt_error(MESSAGES['msg_invalid_float'])
        apr = input()

    return (float(apr) / 12) / 100

def get_duration():
    # get loan duration, verify input, return an integer
    print()
    prompt(MESSAGES['msg_duration'])
    duration = input()

    while invalid_int(duration):
        prompt_error(MESSAGES['msg_invalid_int'])
        duration = input()

    return int(duration)

def run_calculator():
    clear_screen()
    prompt(MESSAGES['msg_welcome'])
    print()

    while True:

        loan_amount = get_loan_amount()
        monthly_apr = get_apr()
        duration = get_duration()

        # calculate monthly payment
        if monthly_apr == 0:
            monthly_payment = loan_amount / duration
        else:
            denominator = (1 - (1 + monthly_apr) ** (-duration))
            monthly_payment = loan_amount * (monthly_apr / denominator)

        print()
        print(f'>>> Your monthly payment will be ${monthly_payment:.2f} <<<')

        print()
        prompt(MESSAGES['msg_calculate_again'])

        again = input()
        if not again or again[0].lower() != 'y':
            print()
            prompt(MESSAGES['msg_end_thanks'])
            print()
            break

        clear_screen()


run_calculator()