from generate_board import generate_board, print_board
from player_choice import get_player_choice

current_player = "X"
board = generate_board()
print_board(board)
for i in range(0, 9):
    board = get_player_choice(board, current_player)
    print_board(board)
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
