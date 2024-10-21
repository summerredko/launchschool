import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

def prompt(message):
    print(f"==> {message}")

def is_player_winner(player, computer):
    winning_combinations = [
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
    return (player, computer) in winning_combinations

def display_winner(player, computer):
    if is_player_winner(player, computer):
        prompt("Player wins!")
        return "player"
    if is_player_winner(computer, player):
        prompt("Computer wins!")
        return "computer"
    prompt("It's a tie!")
    return "tie"

first_letter_to_word = {
    choice[0]: choice for choice in VALID_CHOICES}

number_to_word = {
    '1': "scissors",
    '2': "spock"
}

player_score = 0
computer_score = 0

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while (
        choice not in first_letter_to_word and
        choice not in number_to_word and
        choice not in VALID_CHOICES
    ):
        prompt("That's not a valid choice")
        choice = input().lower()

    if choice == "s":
        prompt("Input 1 for scissors or 2 for spock")
        choice = input()

        while choice not in number_to_word:
            prompt("That's not a valid choice")
            choice = input()

        choice = number_to_word[choice]

    elif choice in first_letter_to_word:
        choice = first_letter_to_word[choice]

    computer_choice = random.choice(VALID_CHOICES)

    winner = display_winner(choice, computer_choice)

    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1

    print(f"Scores: Player {player_score}, Computer {computer_score}")

    if player_score == 3:
        print("You won the match!")
    elif computer_score == 3:
        print("Computer won the match!")

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
