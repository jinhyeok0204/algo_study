from collections import deque
import heapq
def main():
    n, m, start = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        if not (b in graph[a] and a in graph[b]):
            heapq.heappush(graph[a], b)
            heapq.heappush(graph[b], a)
    visited = [False] * (n+1)

    ls = []
    dfs(ls, graph, start, n, visited)
    print(*ls)
    ls2 = []
    bfs(ls2, graph, start, n)
    print(*ls2)


def bfs(ls, graph, start, n):

    visited = [False] * (n+1)
    visited[start] = True
    q = deque([start])

    while q:
        now = q.popleft()
        ls.append(now)

        for neighbors in graph[now]:
            if not visited[neighbors]:
                visited[neighbors] = True
                q.append(neighbors)


def dfs(ls, graph, start, n, visited):

    visited[start] = True

    ls.append(start)

    for neighbors in graph[start]:
        if not visited[neighbors]:
            dfs(ls, graph, neighbors, n, visited)


if __name__ == '__main__':
    main()



