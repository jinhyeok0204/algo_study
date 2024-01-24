from collections import defaultdict


def main():
    t = int(input())
    for _ in range(t):
        print(solution())


def solution():
    n = int(input())

    clothes = []
    for _ in range(n):
        clothes.append(input().split())

    d = defaultdict(list)
    for v, k in clothes:
        d[k].append(v)

    result = 1
    for k in d:
        result *= (len(d[k]) + 1)

    return result - 1

main()

