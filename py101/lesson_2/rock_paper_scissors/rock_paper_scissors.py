import random
import os

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

WINNING_COMBINATIONS = [
        ("scissors", "paper"),
        ("paper", "rock"),
        ("rock", "lizard"),
        ("lizard", "spock"),
        ("spock", "scissors"),
        ("scissors", "lizard"),
        ("lizard", "paper"),
        ("paper", "spock"),
        ("spock", "rock"),
        ("rock", "scissors")
    ]

CHOICE = ""
WINNER = ""
user_score = ""
computer_score = ""

MATCH_WIN = 3

def prompt(message):
    print(f"==> {message}")

def prompt_for_choice():
    global CHOICE
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    CHOICE = input().lower()

def validate_choice():
    global CHOICE
    while (
        CHOICE not in FIRST_LETTER_TO_WORD and
        CHOICE not in number_to_word and
        CHOICE not in VALID_CHOICES
    ):
        prompt("That's not a valid choice")
        CHOICE = input().lower()

def scissors_or_spock():
    global CHOICE
    if CHOICE == "s":
        prompt("Input 1 for scissors or 2 for spock")
        CHOICE = input()

        while CHOICE not in number_to_word:
            prompt("That's not a valid choice")
            CHOICE = input()

        CHOICE = number_to_word[CHOICE]

    elif CHOICE in FIRST_LETTER_TO_WORD:
        CHOICE = FIRST_LETTER_TO_WORD[CHOICE]


def is_winner(user, computer):
    return (user, computer) in WINNING_COMBINATIONS

def display_winner(user, computer):
    if is_winner(user, computer):
        prompt("You win!")
        return "user"
    if is_winner(computer, user):
        prompt("Computer wins!")
        return "computer"
    prompt("It's a tie!")
    return "tie"
def display_scores():
    prompt(f"Scores: Player {user_score}, Computer {computer_score}")

def points_added():
    global user_score
    global computer_score
    if WINNER == "user":
        user_score += 1
    elif WINNER == "computer":
        computer_score += 1

def match_win():
    global user_score
    global computer_score
    if user_score == MATCH_WIN:
        print("You won the match!")
        user_score = 0
        computer_score = 0
    elif computer_score == MATCH_WIN:
        print("Computer won the match!")
        user_score = 0
        computer_score = 0

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def reset_score():
    global user_score
    global computer_score
    user_score = 0
    computer_score = 0


FIRST_LETTER_TO_WORD = {
    CHOICE[0]: CHOICE for CHOICE in VALID_CHOICES}

number_to_word = {
    '1': "scissors",
    '2': "spock"
}

user_score = 0
computer_score = 0

while True:
    prompt_for_choice()
    validate_choice()
    scissors_or_spock()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {CHOICE}, computer chose {computer_choice}')

    WINNER = display_winner(CHOICE, computer_choice)

    points_added()

    display_scores()

    match_win()

    # Do you want to play again?
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer in ['n', 'no', 'y', 'yes']:
            break
        prompt("That's not a valid choice. Please enter 'y' or 'n'.")

    if answer in ['n', 'no']:
        break
    clear_screen()
