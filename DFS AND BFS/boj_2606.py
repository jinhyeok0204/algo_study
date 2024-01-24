from collections import Counter


def main():
    n = int(input())

    pair = int(input())

    adj_list = [[] for _ in range(n+1) ]
    for i in range(pair):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = [False for _ in range(n+1)]

    dfs(adj_list, 1, visited)

    result = Counter(visited)
    print(result[True] - 1)


def dfs(adj_list, node, visited):
    visited[node] = True
    for each in adj_list[node]:
        if visited[each]:
            continue
        dfs(adj_list, each, visited)


main()