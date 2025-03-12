# Let's make the computer defensive-minded so that, 
# when an immediate threat exists, it will try to defend the 3rd square. 
# An immediate threat occurs when the human player has 2 squares in a row 
# with the 3rd square unoccupied. 
# If there's no immediate threat, the computer can pick a random square.

# If a row has two Xs, mark the third space with an O
# If a column has two Xs, mark the third space with an O
# If diagonal has two Xs, mark the third space with an O



def display_board(board):
    os.system('clear')

    prompt(f"Welcome to Tic-Tac-Toe!")
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
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

