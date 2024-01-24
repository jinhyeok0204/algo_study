# 플로이드 워셜 알고리즘은  한 지점에서 특정 지점까지의 최단 경로를 구해야 하는 경우에 사용
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우
# 플로이드 워셜 알고리즘의 시간 복잡도는 O(N^3)이다

# 플로이드 워셜 알고리즘 : 다이나믹 프로그래밍.. 노드의 개수가 N이라고 할 때, N번 만큼으 N단계를 반복하며 점화식에 맞게 2차원 리스트를 갱신한다.
# 각 단계에서는 해당 노드를 거쳐 가는 경우를 고려한다. 예를 들어 1번 노드에 대하서 확인할 때는 1번 노드를 중간에 거쳐 지나가는 모든 경우를 고려한다
# A -> 1 -> B로 가는 비용을 확인한 후에 최단거리를 갱신한다.
# 따라서 현재 확인하고 있는 노드를 제외하고, N-1개의 노드중에서 서로 다른 노드 (A, B)쌍을 선택한다. 이후에 A -> 1 -> B로 가는 비용을 확인한 뒤에 최단 거리를 갱신한다.
# 점화식 : D[a][b] = min(D[a][b], D[a][k] + D[k][b])

def main():
    INF = 1e9
    # 노드, 간선 개수
    v, e = map(int, input())

    graph = [[INF] * (v+1) for _ in range(v+1)]

    # 출발지와 목적지가 같은경우 0으로 초기화
    for i in range(1, v+1):
        for j in range(1, v+1):
            if i == j:
                graph[i][j] = 0

    # 간선에 대한 정보를 입력받고, 그 정보로 초기화
    for _ in range(e):
        # cost of a -> b is c
        a, b, c = map(int, input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, v+1):
        for a in range(1, v+1):
            for b in range(1, v+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])



if __name__ == '__main__':
    main()