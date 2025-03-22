import os
import platform
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
VALID_SHORT_CHOICES = ['r', 'p', 'sc', 'sp', 'l']

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def prompt(message):
    print(f'>-- {message}')

def validate_user_choice(choice):
    while (
        choice not in VALID_CHOICES
        and choice not in VALID_SHORT_CHOICES):
        prompt(f'Please choose: {", ".join(VALID_CHOICES)}.')
        prompt(f'Or: {", ".join(VALID_SHORT_CHOICES)}.')
        choice = input()

    return choice

def convert_short_input(choice):
    match choice:
        case 'r':
            return 'rock'
        case 'p':
            return 'paper'
        case 'sc':
            return 'scissors'
        case 'sp':
            return 'spock'
        case 'l':
            return 'lizard'

def display_winner (user, computer):
    if user == computer:
        prompt(f'You both chose {user}.')
    else:
        prompt(f'You chose {user} and the computer chose {computer}.')

    if ((user == 'rock' and computer in ['scissors', 'lizard'])
        or (user == 'paper' and computer in ['rock', 'spock'])
        or (user == 'scissors' and computer in ['paper', 'lizard'])
        or (user == 'lizard' and computer in ['paper', 'spock'])
        or (user == 'spock' and computer in ['scissors', 'rock'])):
        prompt('You win!')
    elif ((user == 'rock' and computer in ['paper', 'spock'])
        or (user == 'paper' and computer in ['scissors', 'lizard'])
        or (user == 'scissors' and computer in ['rock', 'spock'])
        or (user == 'lizard' and computer in ['rock', 'scissors'])
        or (user == 'spock' and computer in ['lizard', 'paper'])):
        prompt('The computer wins.')
    else:
        prompt('Tie game.')


while True:
    clear_screen()

    prompt(f"Let's play! Please choose: {", ".join(VALID_CHOICES)}.")
    prompt(f"You can enter full words or: {", ".join(VALID_SHORT_CHOICES)}.")
    user_choice = input()

    user_choice = validate_user_choice(user_choice)

    if 1 <= len(user_choice) <= 2:
        user_choice = convert_short_input(user_choice)

    computer_choice = random.choice(VALID_CHOICES)

    print()
    display_winner(user_choice, computer_choice)

    print()
    prompt('Want to play again? (y/n)')
    play_again = input().lower()

    while True:
        if play_again.startswith('y') or play_again.startswith('n'):
            break

        prompt("Please enter 'y' or 'n'")
        play_again = input().lower()

    if play_again[0] == 'n':
        break
