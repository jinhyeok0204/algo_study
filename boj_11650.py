def main():
    n = int(input())
    points = []
    for _ in range(n):
        p = tuple(map(int, input().split()))
        points.append(p)

    points.sort(key=lambda x:(x[0], x[1]))

    for each in points:
        print(*each)

main()