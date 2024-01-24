from collections import deque
def main():

    n = int(input())

    graph = []
    for i in range(n):
        line = list(map(int, input()))
        graph.append(line)

    result = 0 # 단지 수

    step = 0
    counts = [0 for _ in range(1500)]
    for i in range(n):
        for j in range(n):
            if dfs(graph, i, j, n, counts, step):
                result += 1
                step += 1
    print(result)

    counts = [each for each in counts if each != 0]
    counts.sort()
    for each in counts:
        print(each)


def dfs(graph, x, y, n, counts, step):
    # 범위 벗어나면 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    # 방문하지 않았다면
    if graph[y][x] >= 1:
        counts[step] += 1
        graph[y][x] = 0  # 방문 처리
        dfs(graph, x - 1, y, n, counts, step)
        dfs(graph, x + 1, y, n, counts, step)
        dfs(graph, x, y - 1, n, counts, step)
        dfs(graph, x, y + 1, n, counts, step)
        return True
    # 이미 방문했다면
    return False

main()
