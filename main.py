from generate_board import generate_board, print_board
from manage_players import get_player_choice, switch_players
from manage_ending import check_for_winner, print_winner, check_for_tie, print_tie

winner = ""
current_player = "X"
board = generate_board()
print_board(board)
is_tie = False

def main(board, current_player, winner, is_tie):

    while winner == "" and is_tie == False:
        board, current_player = get_player_choice(board, current_player)
        print_board(board)
        current_player = switch_players(current_player)
        winner = check_for_winner(board)
        is_tie = check_for_tie(board, winner)
        print_tie(is_tie)

    print_winner(winner)


main(board, current_player, winner, is_tie)
