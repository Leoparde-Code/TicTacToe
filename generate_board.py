def generate_board():
    board = [[" ", " | "," ", " | ", " "], ["-------------"], [" ", " | "," ", " | ", " "], ["-------------"], [" ", " | "," ", " | ", " "]]
    return board

def print_board(board):
    for i in range(0, 5):
        print(*board[i])
