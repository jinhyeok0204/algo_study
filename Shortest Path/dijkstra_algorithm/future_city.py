# M기업 코딩테스트

import heapq




def main():
    global INF
    INF = 1e9
    # 회사의 개수, 경로의 개수
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        # a -> b, b -> a의 비용 모두 1
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    x, k = map(int, input().split())
    one_to_k = dijkstra(1, graph, k, n)
    k_to_x = dijkstra(k, graph, x, n)

    if one_to_k == INF or k_to_x == INF:
        return -1
    return one_to_k + k_to_x


def dijkstra(start, graph, end, n):

    distance = [INF] * (n+1)

    q = []
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for neighbor in graph[now]:
            cost = dist + 1
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))

    return distance[end]


if __name__ == '__main__':
    print(main())
