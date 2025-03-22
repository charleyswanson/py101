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

def choose_winner(user, computer):
    print()
    if user == computer:
        prompt(f'You both chose {user}.')
    else:
        prompt(f'You chose {user} and the computer chose {computer}.')

    if ((user == 'rock' and computer in ['scissors', 'lizard'])
        or (user == 'paper' and computer in ['rock', 'spock'])
        or (user == 'scissors' and computer in ['paper', 'lizard'])
        or (user == 'lizard' and computer in ['paper', 'spock'])
        or (user == 'spock' and computer in ['scissors', 'rock'])):
        return 'user'
    elif ((user == 'rock' and computer in ['paper', 'spock'])
        or (user == 'paper' and computer in ['scissors', 'lizard'])
        or (user == 'scissors' and computer in ['rock', 'spock'])
        or (user == 'lizard' and computer in ['rock', 'scissors'])
        or (user == 'spock' and computer in ['lizard', 'paper'])):
        return 'computer'
    else:
        return 'tie'

def display_winner(_winner):
    match _winner:
        case 'user':
            prompt('You win!')
        case 'computer':
            prompt('The computer wins.')
        case 'tie':
            prompt('Tie game.')

def scoring(_winner):
    print()
    match _winner:
        case 'user':
            score_card['user'] += 1
        case 'computer':
            score_card['computer'] += 1
        case 'tie':
            score_card['ties'] += 1
    prompt (f'You: {score_card['user']}, '
            f'Computer: {score_card['computer']} '
            f'({score_card['ties']} ties)')

def best_of_five_winner():
    if score_card['user'] == 3:
        prompt('You win the best of five!')
        return False
    elif score_card['computer'] == 3:
        prompt('Computer wins the best of five!')
        return False
    else:
        return True


score_card = {'user': 1, 'computer': 1, 'ties': 0}

continue_best_of_five = True

while continue_best_of_five:
    # clear_screen()

    prompt("Let's play best of five - first one to three wins the game!")
    print()
    prompt(f"Please choose: {", ".join(VALID_CHOICES)}.")
    prompt(f"You can enter full words or: {", ".join(VALID_SHORT_CHOICES)}.")
    user_choice = input()

    user_choice = validate_user_choice(user_choice)

    if 1 <= len(user_choice) <= 2:
        user_choice = convert_short_input(user_choice)

    computer_choice = random.choice(VALID_CHOICES)

    winner = choose_winner(user_choice, computer_choice)
    display_winner(winner)
    scoring(winner)

    best_of_five_winner
    continue_best_of_five = best_of_five_winner()
    print(repr(continue_best_of_five))

    print()
    prompt('Want to keep going on the best of five? (y/n)')
    play_again = input().lower()

    while True:
        if play_again.startswith('y') or play_again.startswith('n'):
            break

        prompt("Please enter 'y' or 'n'")
        play_again = input().lower()

    if play_again[0] == 'n':
        break
