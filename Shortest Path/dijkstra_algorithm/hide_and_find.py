# 이코테 숨박꼭질

import heapq
from collections import Counter
def main():
    INF = int(1e9)
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    distance = [INF] * (n+1)
    dikjstra(graph, distance, 1)

    result = 0
    idx = -1
    for i in range(2, n+1):
        if distance[i] > result:
            result = distance[i]
            idx = i

    count = Counter(distance)[result]

    print(result, idx, count)

def dikjstra(graph, distance, start):

    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for neighbor in graph[now]:
            cost = dist + 1
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))


if __name__ == '__main__':
    main()