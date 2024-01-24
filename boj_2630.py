
def slicing_board(n, row, col):
    global blue_count, white_count
    color = board[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if color != board[i][j]:
                next_size = n // 2
                slicing_board(next_size, row, col)
                slicing_board(next_size, row, col + next_size)
                slicing_board(next_size, row + next_size, col)
                slicing_board(next_size, row+next_size, col+next_size)
                return
    # 모두 색깔이 같은 경우

    if color == 0:
        white_count += 1
    else:
        blue_count += 1



n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

blue_count, white_count = 0, 0
slicing_board(n, 0, 0)
print(white_count)
print(blue_count)

