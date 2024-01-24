from collections import deque

def main():

    n, k = map(int, input().split())

    graph = []
    virus = []
    for i in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
        for j in range(n):
            if graph[i][j] != 0:
                virus.append((i, j, 0, graph[i][j]))
    s, target_x, target_y = map(int, input().split())

    virus.sort(key=lambda each: each[-1])
    bfs(graph, virus, s, target_x, target_y)


def bfs(graph: list[list], virus: list[tuple], target_s: int, target_x: int, target_y: int):
    q = deque(virus)

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y, time, virus_type = q.popleft()
        if time == target_s:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= target_x or ny >= target_y:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_type
                q.append((nx, ny, time+1, virus_type))

    print(graph[target_x-1][target_y-1])


main()
