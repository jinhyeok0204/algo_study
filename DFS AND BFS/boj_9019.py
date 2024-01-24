from collections import deque
from sys import stdin

def main():
    t = int(input())
    for _ in range(t):
        print(solution())


def solution():
    a, b = map(int, stdin.readline().rstrip().split())

    q = deque()
    q.append((a, ""))
    visited = set()
    visited.add(a)
    while q:

        a, command = q.popleft()
        if a == b:
            return command

        else:
            d = a * 2 % 10000
            if d not in visited:
                q.append((d, command + "D"))
                visited.add(d)

            s = (a - 1) % 10000
            if s not in visited:
                q.append((s, command + "S"))
                visited.add(s)

            l = rotate_left(a)
            if l not in visited:
                q.append((l, command + "L"))
                visited.add(l)

            r = rotate_right(a)
            if r not in visited:
                q.append((r, command + "R"))
                visited.add(r)


def rotate_left(a):
    return a // 1000 + (a % 1000) * 10


def rotate_right(a):
    return a // 10 + (a % 10) * 1000


main()