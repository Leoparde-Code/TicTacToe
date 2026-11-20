def get_player_choice(board, current_player):
    try:
        selected_square = int(input("Select a square: "))
        i = selected_square
        if i == 1:
            board[0][0] = current_player
        elif i == 2:
            board[0][2] = current_player
        elif i == 3:
            board[0][4] = current_player
        elif i == 4:
            board[2][0] = current_player
        elif i == 5:
            board[2][2] = current_player
        elif i == 6:
            board[2][4] = current_player
        elif i == 7:
            board[4][0] = current_player
        elif i == 8:
            board[4][2] = current_player
        elif i == 9:
            board[4][4] = current_player
    except Exception:
        raise Exception("Terminated")

    return board
