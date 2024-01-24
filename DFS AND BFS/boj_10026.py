from collections import deque
def main():
    n = int(input())

    graph_original = []
    graph_disease = []

    for i in range(n):
        line = input()
        p_original = []
        p_disease = []

        for each in line:
            p_original.append(each)
            if each == 'G':
                each = 'R'
            p_disease.append(each)

        graph_disease.append(p_disease)
        graph_original.append(p_original)

    visited_original = [[False] * n for _ in range(n)]
    visited_disease = [[False] * n for _ in range(n)]

    count_original = 0
    count_disease = 0

    for i in range(n):
        for j in range(n):
            if not visited_original[i][j]:
                bfs(graph_original, visited_original, n, graph_original[i][j], i, j)
                count_original += 1
            if not visited_disease[i][j]:
                bfs(graph_disease, visited_disease, n , graph_disease[i][j], i, j)
                count_disease += 1

    print(count_original, count_disease)


def bfs(graph, visited, n: int, target_color, i: int, j: int):

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    q = deque()
    q.append((i, j))
    while q:

        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if visited[nx][ny] or graph[nx][ny] != target_color:
                continue

            if graph[nx][ny] == target_color:
                visited[nx][ny] = True
                q.append((nx, ny))


main()

