INF = 1e9


def main():
    global INF
    n, m = map(int, input().split())

    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    result = INF
    minimum = 0
    for i in range(1, n+1):
        if sum(graph[i][1:]) < result:
            result = sum(graph[i][1:])

            minimum = i

    print(minimum)


if __name__ == '__main__':
    main()