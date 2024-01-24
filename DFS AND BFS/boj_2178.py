import sys
from collections import deque

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        line = input().strip()

        int_line = []
        for s in line:
            int_line.append(int(s))
        graph.append(int_line)

    start_point = (0, 0)
    bfs(graph, start_point, n, m)
    print(graph[n-1][m-1])


def bfs(graph: list, start_point: tuple, n: int, m: int):

    q = deque([start_point])

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


main()
