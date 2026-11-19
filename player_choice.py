def get_player_choice(board):
    selected_square = int(input("Select a square: "))
    i = selected_square
    if i == 1:
        board[0][0] = "X"
    elif i == 2:
        board[0][2] = "X"
    elif i == 3:
        board[0][4] = "X"
    elif i == 4:
        board[2][0] = "X"
    elif i == 5:
        board[2][2] = "X"
    elif i == 6:
        board[2][4] = "X"
    elif i == 7:
        board[4][0] = "X"
    elif i == 8:
        board[4][2] = "X"
    elif i == 9:
        board[4][4] = "X"

    return board
