def main():
    INF = int(1e9)
    n, m = map(int, input().split())
    distance = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                distance[i][j] = 0

    for _ in range(m):
        low, high = map(int, input().split())
        distance[low][high] = 1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, k+1):
                distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

    result = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if distance[i][j] != INF or distance[j][i] != INF:
                count += 1
        if count == n:
            result += 1

    print(result)
