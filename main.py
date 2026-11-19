from generate_board import generate_board, print_board
from player_choice import get_player_choice


board = generate_board()
print_board(board)
board = get_player_choice(board)
print_board(board)
