from sys import stdin
from collections import deque


def main():
    n, m = map(int, input().split())
    board = []

    for _ in range(n):
        line = list(map(int, stdin.readline().rstrip().split()))
        board.append(line)

    start_point = find_start_point(board)

    q = deque([start_point])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    result = [[0] * m for _ in range(n)]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if (ny, nx) == start_point:
                continue
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if board[ny][nx] == 0 or result[ny][nx] != 0:
                continue

            result[ny][nx] = result[y][x] + 1
            q.append((ny, nx))

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and result[i][j] == 0:
                result[i][j] = -1

    for line in result:
        print(*line)


def find_start_point(board) -> tuple:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                return i, j


if __name__ == '__main__':
    main()
