def main():
    INF = int(1e9)
    n = int(input())
    graph = []
    for _ in range(n):
        line = list(map(int, input().split()))
        for i in range(len(line)):
            if line[i] == 0:
                line[i] = INF
        graph.append(line)

    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for line in graph:
        for each in line:
            if each >= INF:
                print(0, end=" ")
            else:
                print(1, end=" ")
        print()


main()
