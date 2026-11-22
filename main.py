from generate_board import generate_board, print_board
from player_choice import get_player_choice, switch_players
from get_winner import check_for_winner, print_winner

counter = 1
winner = ""
current_player = "X"
board = generate_board()
print_board(board)
def main(board, current_player, winner, counter):


    while winner == "" and counter <= 9:
        board = get_player_choice(board, current_player)
        print_board(board)
        current_player = switch_players(current_player)
        winner = check_for_winner(board)
        counter += 1

    print_winner(winner)

main(board, current_player, winner, counter)
