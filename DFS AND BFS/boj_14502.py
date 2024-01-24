from sys import stdin
from collections import deque
from itertools import combinations
from copy import deepcopy
from collections import Counter

def main():
    n, m = map(int, input().split())

    board = []
    empty = []
    virus = []
    for i in range(n):
        line = list(map(int, stdin.readline().rstrip().split()))

        for j in range(len(line)):
            if line[j] == 2:
                virus.append((i, j))
            elif line[j] == 0:
                empty.append((i, j))

        board.append(line)

    three_empty_combi = combinations(empty, 3)
    result = 0
    # 아무거나 3개
    for comb in three_empty_combi:
        new_board = deepcopy(board)

        for each in comb:
            x, y = each

            # 벽 세워주기
            new_board[x][y] = 1


        # bfs 수행하기
        q = deque(virus)
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        while q:

            vx, vy = q.popleft()

            for i in range(4):
                nx, ny = vx + dx[i], vy + dy[i]

                if (0 <= nx < n and 0 <= ny < m) and new_board[nx][ny] == 0:
                    new_board[nx][ny] = 2
                    q.append((nx, ny))

        safety_zone = 0
        for line in new_board:
            counter = Counter(line)
            safety_zone += counter[0]

        result = max(result, safety_zone)

    print(result)


main()
