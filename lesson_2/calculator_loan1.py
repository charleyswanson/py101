import json
import os
import platform

# Load the messages from the JSON file
with open('calculator_loan_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'>-- {message}')

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

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while True:
    clear_screen()
    prompt(MESSAGES['msg_welcome'])
    prompt(MESSAGES['msg_inputs'])

    # get loan amount, verify input, convert to integer
    print()
    prompt(MESSAGES['msg_loan_amount'])
    print('$', end='')
    loan_amount = input()

    while invalid_int(loan_amount):
        prompt(MESSAGES['msg_invalid_int'])
        loan_amount = input()

    loan_amount = int(loan_amount)

    # get APR, verify input, convert to montly APR
    print()
    prompt(MESSAGES['msg_apr'])
    apr = input()

    while invalid_float(apr):
        prompt(MESSAGES['msg_invalid_float'])
        apr = input()

    monthly_apr = (float(apr) / 12) / 100

    # get loan duration, error check, convert to integer
    print()
    prompt(MESSAGES['msg_duration'])
    duration = input()

    while invalid_int(duration):
        prompt(MESSAGES['msg_invalid_int'])
        duration = input()

    duration = int(duration)

    # calculate monthly payment
    if apr == '0':
        monthly_payment = loan_amount / duration
    else:
        denominator = (1 - (1 + monthly_apr) ** (-duration))
        monthly_payment = loan_amount * (monthly_apr / denominator)

    print()
    print(f'--> Your monthly payment will be ${monthly_payment:.2f}')

    print()
    prompt(MESSAGES['msg_calculate_again'])

    again = input()
    if not again or again[0].lower() != 'y':
        prompt(MESSAGES['msg_end_thanks'])
        print()
        break