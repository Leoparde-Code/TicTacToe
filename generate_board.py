def generate_board(board, row):
    for i in range(0, 3):
        print(*board[i])
        if i == 2:
            break
        else:
            print(*row)
