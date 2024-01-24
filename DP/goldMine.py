def main():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())

        gold_mine = list(map(int, input().split()))
        ary = []
        for i in range(n):
            ary.append(gold_mine[i*m:i*m+m])
        d = [[0] * n for _ in range(m)]

        d[0][0], d[1][0], d[2][0] = ary[0][0], ary[1][0], ary[2][0]

        for i in range(1,m):
            for j in range(1, n):
                d[]



main()



