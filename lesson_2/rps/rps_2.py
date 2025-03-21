import os
import platform
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def prompt(message):
    print(f'>-- {message}')

def display_winner (user, computer):
    if user == computer:
        print(f'user: {user} / computer: {computer}')
        prompt(f'You both chose {user}.')
    else:
        print(f'user: {user} / computer: {computer}')
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
    user_choice = input()

    while user_choice not in VALID_CHOICES:
        prompt(f'Please choose: {", ".join(VALID_CHOICES)}.')
        user_choice = input()

    computer_choice = random.choice(VALID_CHOICES)

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
