def main():
    n, k = map(int, input().split())

    board = list(map(str, range(1, n+1)))

    idx = k - 1
    result = []

    while n != 1:
        to_remove = board[idx]
        result.append(to_remove)
        board.remove(to_remove)
        idx += (k - 1)
        if idx >= len(board):
            idx = idx % len(board)
        n -= 1
    result.append(board[0])

    print("<" + ", ".join(result) + ">")


if __name__ == '__main__':
    main()
