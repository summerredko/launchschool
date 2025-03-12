import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_SCORE = 5
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]

def prompt(message):
    print(f"=> {message}")

def display_board(board):
    os.system('clear')

    prompt("Welcome to Tic-Tac-Toe!")
    prompt(f"Player is '{HUMAN_MARKER}'. Computer is '{COMPUTER_MARKER}'.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(lst, delimiter=', ', conjunction='or'):
    if len(lst) == 1:
        return str(lst[0])
    if len(lst) == 2:
        return str(lst[0]) + ' or ' + str(lst[1])
    if len(lst) == 0:
        return ""

    result = ""
    for i in range(len(lst) - 1):
        result += str(lst[i])
        if i < len(lst) - 1:
            result += delimiter

    result += conjunction + " "
    result += str(lst[-1])

    return result

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            board[int(square)] = HUMAN_MARKER
            break

        prompt("Sorry, that's not a valid choice.")

def computer_chooses_square(board):
    if not empty_squares(board):
        return

    def find_best_move(marker):
        for line in WINNING_LINES:
            sq1, sq2, sq3 = line
            if (board[sq1] == marker and board[sq2] == marker and
                board[sq3] == INITIAL_MARKER):
                return sq3
            if (board[sq2] == marker and board[sq3] == marker and
                board[sq1] == INITIAL_MARKER):
                return sq1
            if (board[sq1] == marker and board[sq3] == marker and
                board[sq2] == INITIAL_MARKER):
                return sq2
        return None

    move = find_best_move(COMPUTER_MARKER)
    if move is None:
        move = find_best_move(HUMAN_MARKER)

    if move is not None:
        board[move] = COMPUTER_MARKER
        return

    if board[5] == INITIAL_MARKER:
        board[5] = COMPUTER_MARKER
        return  

    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        if (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def match_win(winner, match_score_player, match_score_computer):
    if winner == 'Player':
        match_score_player += 1
    elif winner == 'Computer':
        match_score_computer += 1
    return match_score_player, match_score_computer

def game_winner(match_score_player, match_score_computer):
    if match_score_player == WINNING_SCORE:
        prompt('Congratulations, Player won the match!')
        return 'Player'
    if match_score_computer == WINNING_SCORE:
        prompt('Sorry, Computer won the match.')
        return 'Computer'
    return None

def reset_scores():
    return 0, 0

def who_first():
    while True:
        prompt('Who would you like to go first: Player or Computer? (p or c)')
        choice = input().strip().lower()

        if choice == 'p':
            return 'Player'
        if choice == 'c':
            return 'Computer'
        prompt("""Invalid choice.
                Please enter 'p' for Player or 'c' for Computer.""")

def alternate_player(current_player):
    return 'Computer' if current_player == 'Player' else 'Player'

def choose_square(board, current_player):
    if current_player == 'Player':
        return player_chooses_square(board)
    return computer_chooses_square(board)

def play_tic_tac_toe():
    match_score_player = 0
    match_score_computer = 0
    while True:
        board = initialize_board()

        display_board(board)
        current_player = who_first()

        while True:
            display_board(board)
            choose_square(board, current_player)
            if someone_won(board) or board_full(board):
                break
            current_player = alternate_player(current_player)

        display_board(board)

        winner = detect_winner(board)
        match_score_player, match_score_computer = match_win(
            winner, match_score_player, match_score_computer)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
            prompt(f"""Player score: {match_score_player} """
                   f"""Computer score: {match_score_computer}""")
        else:
            prompt("It's a tie!")

        if game_winner(match_score_player, match_score_computer):
            match_score_player, match_score_computer = reset_scores()

        while True:
            answer = input("Play again? (y or n): ").strip().lower()

            if answer in ['y', 'n']:
                break
            prompt("Input Invalid. Please enter 'y' or 'n'.")

        if answer == 'n':
            prompt('Thanks for playing Tic Tac Toe!')
            break

play_tic_tac_toe()
