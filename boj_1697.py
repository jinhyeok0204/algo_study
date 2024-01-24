from collections import deque


def main():
    n, k = map(int, input().split())
    location = [0] * 100001

    print(bfs(n, k, location))


def bfs(start, end, location):

    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        if now == end:
            return location[now]

        for i in (now-1,now+1,now*2):
            if 0 <= i <= 100000 and not location[i]:
                location[i] = location[now] + 1
                q.append(i)
    return None


if __name__ == '__main__':
    main()

