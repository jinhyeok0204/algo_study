def main():
    n = int(input())

    triangle = []
    d = []
    for i in range(n):
        line = list(map(int, input().split()))
        triangle.append(line)
        length = len(line)
        d.append([0 for _ in range(length)])

    d[0][0] = triangle[0][0]

    for y in range(1, n):
        for x in range(y + 1):
            if x == 0:
               left = d[y-1][x]
               right = 0
            elif x == y:
                left = 0
                right = d[y-1][x-1]
            else:
                left = d[y-1][x-1]
                right = d[y-1][x]

            d[y][x] = triangle[y][x] + max(left, right)

    #print(d)
    print(max(d[n-1]))


main()
