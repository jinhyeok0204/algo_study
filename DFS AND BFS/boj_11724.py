from collections import deque
import sys

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    adj_list = [[] for _ in range(n+1)]

    for i in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [False for _ in range(n+1)]

    count = 0
    for i in range(1, n+1):
        if not visited[i]:
            bfs(adj_list, i, visited)
            count += 1

    print(count)


def bfs(adj_list, start_node, visited):

    q = deque([start_node])

    visited[start_node] = True

    while q:
        u = q.popleft()
        for each in adj_list[u]:
            if not visited[each]:
                q.append(each)
                visited[each] = True


main()
