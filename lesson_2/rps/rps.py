import os
import platform
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
VALID_SHORT_CHOICES = ['r', 'p', 'sc', 'sp', 'l']

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def prompt(message):
    print(f'--> {message}')

def validate_user_choice(choice):
    while (
        choice not in VALID_CHOICES
        and choice not in VALID_SHORT_CHOICES):
        prompt(f'Please choose: {", ".join(VALID_CHOICES)}.')
        prompt(f'Or: {", ".join(VALID_SHORT_CHOICES)}.')
        choice = input().lower()

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

def display_choices(user, computer):
    if user == computer:
        prompt(f'You both chose {user}.')
    else:
        prompt(f'You chose {user} and the computer chose {computer}.')

def player_wins(choice1, choice2):
    return choice2 in WINNING_COMBOS[choice1]

def display_winner(_winner):
    match _winner:
        case 'user':
            prompt('You won that round.')
        case 'computer':
            prompt('The computer won that round.')
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

    if score_card['user'] < 3 and score_card['computer'] < 3:
        if score_card['ties'] == 1:
            prompt (f"Score: You've won {score_card['user']} / "
                f"The computer has won {score_card['computer']}  "
                f"({score_card['ties']} tie)")
        else:
            prompt (f"Score: You've won {score_card['user']} / "
                f"The computer has won {score_card['computer']}  "
                f"({score_card['ties']} ties)")

def display_final_score():
    prompt(f'Final score = You: {score_card['user']} / '
        f'Computer: {score_card['computer']}')

def best_of_five_winner():
    if score_card['user'] == 3:
        prompt('GAME OVER: You won the best of five!')
        display_final_score()
        return False
    if score_card['computer'] == 3:
        prompt('GAME OVER: The computer won the best of five.')
        display_final_score()
        return False
    return True

def play_again():
    prompt('Want to play again? (y/n)')
    again = input().lower()

    while True:
        if again in ['y', 'n', 'yes', 'no']:
            break

        prompt("Please enter 'y' or 'n'")
        again = input().lower()

    if again in ['n', 'no']:
        return False

    return True


clear_screen()
prompt(f"Welcome to {", ".join(VALID_CHOICES).title()}!")
prompt("We'll play best of five - first one to three wins the game.")
print()

score_card = {'user': 0, 'computer': 0, 'ties': 0}
continue_best_of_five = True

while True:
    while continue_best_of_five:
        prompt(f"Please choose: {", ".join(VALID_CHOICES)}.")
        prompt(f"You can enter full words or: "
               f"{", ".join(VALID_SHORT_CHOICES)}.")
        user_choice = input().lower()

        user_choice = validate_user_choice(user_choice)

        if 1 <= len(user_choice) <= 2:
            user_choice = convert_short_input(user_choice)

        computer_choice = random.choice(VALID_CHOICES)

        clear_screen()

        display_choices(user_choice, computer_choice)

        if player_wins(user_choice, computer_choice):
            winner = 'user'
        elif player_wins(computer_choice, user_choice):
            winner = 'computer'
        else:
            winner = 'tie'

        display_winner(winner)
        scoring(winner)

        continue_best_of_five = best_of_five_winner()
        print()

    if play_again() is False:
        print()
        prompt('Hope you had fun!')
        print()
        break

    score_card = {'user': 0, 'computer': 0, 'ties': 0}
    continue_best_of_five = True
    clear_screen()