import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock") or
        (player == "rock" and computer == "lizard") or
        (player == "lizard" and computer == "spock") or
        (player == "spock" and computer == "scissors") or
        (player == "scissors" and computer == "lizard") or
        (player == "lizard" and computer == "paper") or
        (player == "paper" and computer == "spock") or
        (player == "spock" and computer == "rock") or
        (player == "rock" and computer == "scissors")):
        prompt("You win!")
    elif ((player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock") or
        (player == "rock" and computer == "lizard") or
        (player == "lizard" and computer == "spock") or
        (player == "spock" and computer == "scissors") or
        (player == "scissors" and computer == "lizard") or
        (player == "lizard" and computer == "paper") or
        (player == "paper" and computer == "spock") or
        (player == "spock" and computer == "rock") or
        (player == "rock" and computer == "scissors")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

first_letter_to_word = {
    choice[0]: choice for choice in VALID_CHOICES}

number_to_word = {
    '1': "scissors",
    '2': "spock"
}

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while (
        choice not in VALID_CHOICES and 
        choice not in first_letter_to_word and 
        choice not in number_to_word
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

    display_winner(choice, computer_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
