def get_player_choice(board, current_player):
    try:
        selected_square = int(input("Select a square: "))
        i = selected_square
        if i == 1:
            if board[0][0] == ' ':
                board[0][0] = current_player
        elif i == 2:
            if board[0][2] == ' ':
                board[0][2] = current_player
        elif i == 3:
            if board[0][4] == ' ':
                board[0][4] = current_player
        elif i == 4:
            if board[2][0] == ' ':
                board[2][0] = current_player
        elif i == 5:
            if board[2][2] == ' ':
                board[2][2] = current_player
        elif i == 6:
            if board[2][4] == ' ':
                board[2][4] = current_player
        elif i == 7:
            if board[4][0] == ' ':
                board[4][0] = current_player
        elif i == 8:
            if board[4][2] == ' ':
                board[4][2] = current_player
        elif i == 9:
            if board[4][4] == ' ':
                board[4][4] = current_player
    except Exception:
        raise Exception("Terminated")

    return board

def switch_players(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    return current_player
