def get_player_choice(board, current_player):

    selected_square = input("Select a square: ")
    try:
        i = int(selected_square)
        if i == 1:
            if board[0][0] == ' ':
                board[0][0] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 2:
            if board[0][2] == ' ':
                board[0][2] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 3:
            if board[0][4] == ' ':
                board[0][4] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 4:
            if board[2][0] == ' ':
                board[2][0] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 5:
            if board[2][2] == ' ':
                board[2][2] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 6:
            if board[2][4] == ' ':
                board[2][4] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 7:
            if board[4][0] == ' ':
                board[4][0] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 8:
            if board[4][2] == ' ':
                board[4][2] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
        elif i == 9:
            if board[4][4] == ' ':
                board[4][4] = current_player
            else:
                print("Invalid Position")
                current_player = switch_players(current_player)
    except ValueError:
        print("Invalid character")
        current_player = switch_players(current_player)


    return board, current_player

def switch_players(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    return current_player
