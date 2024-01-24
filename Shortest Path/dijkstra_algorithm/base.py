# 다익스트라 알고리즘 : 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
# 개선된 다익스트라 알고리즘 -> O(ElogV) .. V는 노드의 개수 E는 간선의 개수

import heapq

def main():
    INF = int(1e9)
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        # a에서 b로 가는 비용이 c
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(graph, start, distance)


def dijkstra(graph, start_node, distance):

    q = []
    heapq.heappush(q, (0, start_node))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for neighbor in graph[node]:
            cost = dist + neighbor[1]
            if cost < distance[neighbor[0]]:
                distance[neighbor[0]] = cost
                heapq.heappush(q, (cost, neighbor[0]))

