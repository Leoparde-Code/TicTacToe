def check_for_winner(board):
    winner = ""
    if ((board[0][0] == "X" and board[0][2] == "X" and board[0][4] == "X") or
        (board[2][0] == "X" and board[2][2] == "X" and board[2][4] == "X") or
        (board[4][0] == "X" and board[4][2] == "X" and board[4][4] == "X") or
        (board[0][0] == "X" and board[2][0] == "X" and board[4][0] == "X") or
        (board[0][2] == "X" and board[2][2] == "X" and board[4][2] == "X") or
        (board[0][4] == "X" and board[2][4] == "X" and board[4][4] == "X") or
        (board[0][0] == "X" and board[2][2] == "X" and board[4][4] == "X") or
        (board[0][4] == "X" and board[2][2] == "X" and board[4][0] == "X")):
            winner = "X"
    elif ((board[0][0] == "O" and board[0][2] == "O" and board[0][4] == "O") or
        (board[2][0] == "O" and board[2][2] == "O" and board[2][4] == "O") or
        (board[4][0] == "O" and board[4][2] == "O" and board[4][4] == "O") or
        (board[0][0] == "O" and board[2][0] == "O" and board[4][0] == "O") or
        (board[0][2] == "O" and board[2][2] == "O" and board[4][2] == "O") or
        (board[0][4] == "O" and board[2][4] == "O" and board[4][4] == "O") or
        (board[0][0] == "O" and board[2][2] == "O" and board[4][4] == "O") or
        (board[0][4] == "O" and board[2][2] == "O" and board[4][0] == "O")):
            winner = "O"

    return winner

def check_for_tie(board, winner):
    is_tie = False
    if winner == "":
        if (board[0][0] != " " and board[0][2] != " " and board[0][4] != " " and
            board[2][0] != " " and board[2][2] != " " and board[2][4] != " " and
            board[4][0] != " " and board[4][2] != " " and board[4][4] != " "):
                is_tie = True

    return is_tie

def print_winner(winner):
    if winner == "X":
        print("X Wins!")
    elif winner == "O":
        print("O Wins")

def print_tie(is_tie):
    if is_tie:
        print("Tie!")
        return True
