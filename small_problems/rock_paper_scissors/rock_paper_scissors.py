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
    elif ((computer== "scissors" and player == "paper") or
        (computer == "paper" and player == "rock") or
        (computer == "rock" and player == "lizard") or
        (computer == "lizard" and player == "spock") or
        (computer == "spock" and player == "scissors") or
        (computer == "scissors" and player == "lizard") or
        (computer == "lizard" and player == "paper") or
        (computer == "paper" and player == "spock") or
        (computer == "spock" and player == "rock") or
        (computer == "rock" and player == "scissors")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def keep_score(player, computer):
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
        return "player"
    elif ((computer == "scissors" and player == "paper") or
          (computer == "paper" and player == "rock") or
          (computer == "rock" and player == "lizard") or
          (computer == "lizard" and player == "spock") or
          (computer == "spock" and player == "scissors") or
          (computer == "scissors" and player == "lizard") or
          (computer == "lizard" and player == "paper") or
          (computer == "paper" and player == "spock") or
          (computer == "spock" and player == "rock") or
          (computer == "rock" and player == "scissors")):
        return "computer"
    else:
        return "tie"
# def match_winner(player, computer):

#     if winner == "player":
#         player_score += 1
#     elif winner == "computer":
#         computer_score += 1
    
#     return player_score, computer_score

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
    winner = keep_score(choice, computer_choice)

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
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
