from sys import stdin
from collections import deque


def main():
    n, m = map(int, input().split())

    board = []

    for i in range(n):
        line = list( stdin.readline().rstrip())

        for j in range(m):
            if line[j] == "I":
                do_yeon = (i, j)
        board.append(line)

    q = deque()
    q.append(do_yeon)

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    count = 0

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:

                if board[nx][ny] == "P":

                    q.append((nx, ny))
                    board[nx][ny] = "X"
                    count += 1

                elif board[nx][ny] == "O":
                    q.append((nx, ny))
                    board[nx][ny] = "X"

    print(count) if count > 0 else print("TT")


if __name__ == '__main__':
    main()


